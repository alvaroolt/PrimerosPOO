package primerosPOO.fracciones;

public class TestFraccion {

	public static void main(String[] args) {
		Fraccion fraccion1 = new Fraccion(1, 2);
		Fraccion fraccion2 = new Fraccion(2, 3);
		//Fraccion fraccion3 = new Fraccion(7, 6);
		//Fraccion fraccion4 = new Fraccion(1, 4);
		// Fraccion fraccion5 = new Fraccion(5,0);
		// Fraccion fraccion6 = new Fraccion(6,0);
		// Fraccion fraccion7 = new Fraccion(8,0);
		// Fraccion fraccion8 = new Fraccion(9,0);

		System.out.println(fraccion1);
		System.out.println(fraccion2);
		fraccion1.calculaMCM(fraccion2);
		System.out.println(fraccion1);
		System.out.println(fraccion2);
		fraccion1.suma(fraccion2);
		// System.out.println(fraccion1.toString());
		// System.out.println(fraccion2.toString());
		// System.out.println(fraccion3.toString());
		// System.out.println(fraccion4.toString());
		// fraccion4.multiplica(3);
		// System.out.println(fraccion4);
		//fraccion1.multiplica(fraccion3);
		System.out.println(fraccion1);
		System.out.println(fraccion2);
	}

}
