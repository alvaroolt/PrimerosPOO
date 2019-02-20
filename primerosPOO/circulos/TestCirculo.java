package primerosPOO.circulos;

/**
 * 
 * @author Alvaro Leiva Toledano
 *
 */
public class TestCirculo {

	public static void main(String[] args) {
		Circulo circulo1 = new Circulo(3);
		System.out.println(circulo1);
		circulo1.crece(27);
		System.out.println(circulo1);
		circulo1.mengua(10);
		System.out.println(circulo1);
	}
}
