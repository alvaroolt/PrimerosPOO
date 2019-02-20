package primerosPOO.fracciones;

/**
 * Crea una clase Fraccion (en Java yPython) de forma que podamos hacer las
 * siguientes operaciones:
 * 
 * 1. Contruir un objeto Fraccion pasándole al constructor el numerador y el
 * denominador. 2. Obtener la fracción. 3. Obtener y modificar numerador y
 * denominador. 4. No se puede dividir por cero. 5. Obtener resultado de la
 * fracción (número real). 6. Multiplicar la fracción por un número. 7.
 * Multiplicar, sumar y restar fracciones. 8. Simplificar la fracción.
 * 
 * @author Álvaro Leiva Toledano
 * @version 1.0
 */
public class Fraccion {
	
	private int numerador; // numerador
	private int denominador; // denominador

	public Fraccion(int numerador, int denominador) {
		setNumerador(numerador);
		setDenominador(denominador);
	}

	private void setNumerador(int n) {
		this.numerador = n;
	}

	public int getNumerador() {
		return this.numerador;
	}

	private void setDenominador(int d) {
		if (d == 0) {
			System.out.println("El denominador no puede ser cero. Lo transformo en 1");
			d = 1;
		}
		this.denominador = d;
	}

	public int getDenominador() {
		return this.denominador;
	}

	public float getReal() {
		return ((float) getNumerador() / getDenominador());
	}

	public void multiplica(int x) {
		this.numerador = getNumerador() * x;
		this.denominador = getDenominador() * 1;
	}

	public void multiplica(Fraccion fraccion) {
		this.numerador = this.numerador * fraccion.getNumerador();
		this.denominador = this.denominador * fraccion.getDenominador();
	}

	public void suma(Fraccion fraccion) {
		if (this.denominador != fraccion.getDenominador()) {
			System.out.println("No pueden sumarse fracciones de diferente denominador.");
		} else {
			this.numerador += fraccion.getNumerador();
		}
	}

	public void resta(Fraccion fraccion) {
		if (this.denominador != fraccion.getDenominador()) {
			System.out.println("No pueden restarse fracciones de diferente denominador.");
		} else {
			this.numerador = fraccion.getNumerador() - this.numerador;
		}
	}

	public void calculaMCM(Fraccion fraccion1) {
		int min = Math.min(this.denominador, fraccion1.getNumerador());
		// averiguo el minimo de entre los denominadores
		int mcm = 0; // mínimo común múltiplo
		for (int i = 1; i <= min; i++) {
			if (this.denominador % i == 0 && fraccion1.getDenominador() % i == 0) {
				int mcd = i;
				mcm = (this.denominador * fraccion1.getDenominador()) / mcd;
			}
		}
		System.out.println("El mínimo común múltiplo de los denominadores es " + mcm);
		System.out.println("A continuación, igualaré ambas fracciones al mismo demonimador (mcm)");
		// el siguiente cálculo consiste en dividir el mcm por el denominador anterior
		// de cada fracción. De esta manera averiguamos el valor por el que se debe
		// multiplicar el numerador para que sea equivalente al nuevo denominador(es
		// decir, el mcm)
		int nuevoNumerador1 = (mcm / this.denominador) * this.numerador;
		int nuevoNumerador2 = (mcm / fraccion1.getDenominador()) * fraccion1.getNumerador();
		// fraccion1= new Fraccion(nuevoNumerador1,mcm);
		this.numerador = nuevoNumerador1;
		this.denominador = mcm;
		fraccion1.setNumerador(nuevoNumerador2);
		fraccion1.setDenominador(mcm);
	}

	public void simplifica() {
		if (this.numerador == this.denominador) {
			this.numerador = 1;
			this.denominador = 1;
		}
	}

	public String toString() {
		String mensaje = getNumerador() + "/" + getDenominador() + " Resultado = " + getReal();
		return mensaje;

	}
}
