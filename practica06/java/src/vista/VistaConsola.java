package vista;

import modelo.PruebasEstadisticas.ResultadoChi2;
import modelo.PruebasEstadisticas.ResultadoKS;
import modelo.MonteCarloPi.ResultadoPi;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Locale;

/** Vista: salida por consola y gráficos PNG (Java2D, funciona sin pantalla). */
public class VistaConsola {

    private static void f(String fmt, Object... args) {
        System.out.print(String.format(Locale.US, fmt, args));
    }

    public void titulo(String texto) {
        System.out.println("\n" + "=".repeat(78));
        System.out.println(texto);
        System.out.println("=".repeat(78));
    }

    public void mostrarSecuencia(double[] datos, int cuantos) {
        System.out.println("Primeros " + cuantos + " números generados:");
        StringBuilder sb = new StringBuilder("  ");
        for (int i = 0; i < cuantos; i++) {
            sb.append(String.format(Locale.US, "%.8f", datos[i]));
            if (i < cuantos - 1) sb.append(", ");
        }
        System.out.println(sb);
        System.out.println("Total generados: " + datos.length);
    }

    public void mostrarChi2(ResultadoChi2 r, int k) {
        System.out.println("\n--- Prueba Chi-cuadrado ---");
        f("%-16s%12s%12s%n", "Intervalo", "Observada", "Esperada");
        for (int i = 0; i < k; i++) {
            f("[%.1f, %.1f)     %12d%12.1f%n", (double) i / k, (double) (i + 1) / k,
                    r.observadas()[i], r.esperada());
        }
        f("Chi² = %.4f | gl = %d | p = %.6f%n", r.estadistico(), r.gradosLibertad(), r.pValor());
        decision(r.rechazaH0());
    }

    public void mostrarKS(ResultadoKS r) {
        System.out.println("\n--- Prueba Kolmogorov-Smirnov ---");
        f("D+ = %.6f | D- = %.6f%n", r.dMas(), r.dMenos());
        f("D  = %.6f | p = %.6f%n", r.estadistico(), r.pValor());
        decision(r.rechazaH0());
    }

    private void decision(boolean rechaza) {
        if (rechaza) System.out.println("Decisión (α=0.05): p < 0.05 -> SE RECHAZA H0 (no es uniforme).");
        else System.out.println("Decisión (α=0.05): p >= 0.05 -> NO SE RECHAZA H0 (compatible con U(0,1)).");
    }

    public record FilaComparacion(String nombre, ResultadoChi2 chi2, ResultadoKS ks) {}

    public void mostrarComparacion(List<FilaComparacion> filas) {
        f("%n%-22s%10s%12s%10s%10s%12s%10s%n", "Configuración", "Chi²", "p(χ²)", "Dec.",
                "D (KS)", "p(KS)", "Dec.");
        for (FilaComparacion fila : filas) {
            f("%-22s%10.3f%12.5f%10s%10.5f%12.5f%10s%n", fila.nombre(),
                    fila.chi2().estadistico(), fila.chi2().pValor(),
                    fila.chi2().rechazaH0() ? "Rechaza" : "No rech.",
                    fila.ks().estadistico(), fila.ks().pValor(),
                    fila.ks().rechazaH0() ? "Rechaza" : "No rech.");
        }
    }

    public void mostrarTablaPi(List<ResultadoPi> filas) {
        f("%n%10s%14s%14s%18s%n", "N", "π estimado", "Error", "Tiempo Java (s)");
        for (ResultadoPi r : filas) {
            f("%10d%14.6f%14.6f%18.4f%n", r.n(), r.piEstimado(), r.error(), r.tiempoS());
        }
    }

    public void mensaje(String texto) {
        System.out.println(texto);
    }

    // ---------------- gráfico (histograma + FDA) ----------------
    public void graficar(ResultadoChi2 chi2, ResultadoKS ks, String ruta, String titulo) {
        int w = 1100, h = 470;
        BufferedImage img = new BufferedImage(w, h, BufferedImage.TYPE_INT_RGB);
        Graphics2D g = img.createGraphics();
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, w, h);
        g.setColor(Color.BLACK);
        g.setFont(new Font("SansSerif", Font.BOLD, 14));
        g.drawString(titulo, 20, 24);
        g.setFont(new Font("SansSerif", Font.PLAIN, 12));

        // Panel 1: histograma
        int x0 = 60, y0 = 60, pw = 450, ph = 340;
        g.drawString("Histograma (Chi-cuadrado)", x0, y0 - 8);
        g.drawRect(x0, y0, pw, ph);
        int k = chi2.observadas().length;
        int max = 0;
        for (int o : chi2.observadas()) max = Math.max(max, o);
        double ymax = Math.max(max, chi2.esperada()) * 1.15;
        int bw = pw / k;
        g.setColor(new Color(0x3b6ea5));
        for (int i = 0; i < k; i++) {
            int bh = (int) (chi2.observadas()[i] / ymax * ph);
            g.fillRect(x0 + i * bw + 2, y0 + ph - bh, bw - 4, bh);
        }
        g.setColor(Color.RED);
        int ye = y0 + ph - (int) (chi2.esperada() / ymax * ph);
        g.drawLine(x0, ye, x0 + pw, ye);
        g.drawString("Esperada = " + chi2.esperada(), x0 + 5, ye - 5);
        g.setColor(Color.BLACK);
        for (int i = 0; i < k; i++) g.drawString(String.format(Locale.US, "%.1f", (double) i / k),
                x0 + i * bw + 8, y0 + ph + 16);

        // Panel 2: FDA empírica vs teórica
        int x1 = 600;
        g.drawString(String.format(Locale.US, "FDA acumulada (KS: D=%.4f)", ks.estadistico()), x1, y0 - 8);
        g.drawRect(x1, y0, pw, ph);
        double[] ord = ks.ordenados();
        int n = ord.length;
        int paso = Math.max(1, n / 2000);
        g.setColor(new Color(0x3b6ea5));
        int px = x1, py = y0 + ph;
        for (int i = 0; i < n; i += paso) {
            int cx = x1 + (int) (ord[i] * pw);
            int cy = y0 + ph - (int) ((i + 1.0) / n * ph);
            g.drawLine(px, py, cx, cy);
            px = cx;
            py = cy;
        }
        g.setColor(Color.RED);
        g.setStroke(new BasicStroke(1f, BasicStroke.CAP_BUTT, BasicStroke.JOIN_MITER, 10f,
                new float[]{6f, 6f}, 0f));
        g.drawLine(x1, y0 + ph, x1 + pw, y0);
        g.setStroke(new BasicStroke(1f));
        g.setColor(new Color(0x3b6ea5));
        g.drawString("F_n(x) empírica", x1 + 10, y0 + 18);
        g.setColor(Color.RED);
        g.drawString("F(x) teórica U(0,1)", x1 + 10, y0 + 34);
        g.dispose();
        try {
            File archivo = new File(ruta);
            if (archivo.getParentFile() != null) archivo.getParentFile().mkdirs();
            ImageIO.write(img, "png", archivo);
            System.out.println("Gráfico guardado en: " + ruta);
        } catch (IOException e) {
            System.out.println("No se pudo guardar el gráfico: " + e.getMessage());
        }
    }
}
