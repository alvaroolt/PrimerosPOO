package primerosPOO.circulos;

import java.util.Scanner;

/**
 * Crea la clase “Circulo” en Java que responda al siguiente comportamiento:
 * 
 * Un círculo puede crecer. Aumenta su radio. Un círculo puede menguar.
 * Decrementa su radio. Un círculo me devuelve su área si se la pido. Un círculo
 * me dice su estado, por ejemplo “Soy un círculo de radio 0.5 metros. Ocupo un
 * área de 0.7853981633974483 metros cuadrados” (método toString()) 3. Crea una
 * clase TestCirculo que cree una instancia de “Circulo”, muestre su estado, lo
 * haga crecer 27 veces, averigüe su área, lo haga decrecer 10 veces y muestre
 * su estado final.
 * 
 * @author Alvaro Leiva Toledano
 * @version 0.9
 */
public class Circulo {
	//Scanner sc = new Scanner(System.in);
	private int radio;
	
	public Circulo(int radio) {
		setRadio(radio);
	}

	public void setRadio(int r) {
		this.radio = r;
	}

	public int getRadio() {
		return this.radio;
	}

	public void crece(int aumento) {
		if (aumento < 0) {
			System.out.println("Error al aumentar el radio.");
		} else {
			this.radio += aumento;
			System.out.println("Radio aumentado correctamente.");
		}
	}

	public void mengua(int disminucion) {
		if (disminucion < 0) {
			disminucion *= -1;
		}
		this.radio -= disminucion;
		System.out.println("Radio disminuido correctamente.");
	}

	private float calcularArea() {
		float area = (float) (Math.PI * (Math.pow(this.radio, 2)));
		return area;
	}

	public String toString() {
		String mensaje = "¡Hola! Soy un círculo de radio " + getRadio() + "m y de área " + calcularArea() + "m^2.";
		return mensaje;
	}

}
