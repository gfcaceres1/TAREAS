using System;

namespace FigurasGeometricas
{
    class Program
    {
        static void Main(string[] args)
        {
            // Creamos un círculo con radio 5
            Circulo miCirculo = new Circulo(5);
            Console.WriteLine("El área del círculo es: " + miCirculo.CalcularArea());
            Console.WriteLine("El perímetro del círculo es: " + miCirculo.CalcularPerimetro());

            // Creamos un cuadrado con lado 4
            Cuadrado miCuadrado = new Cuadrado(4);
            Console.WriteLine("El área del cuadrado es: " + miCuadrado.CalcularArea());
            Console.WriteLine("El perímetro del cuadrado es: " + miCuadrado.CalcularPerimetro());

            Console.ReadLine();
        }
    }

    // Clase base para representar una figura geométrica
    public abstract class Figura
    {
        // Método abstracto para calcular el área
        public abstract double CalcularArea();

        // Método abstracto para calcular el perímetro
        public abstract double CalcularPerimetro();
    }

    // Clase derivada de Figura para representar un círculo
    public class Circulo : Figura
    {
        // Radio del círculo
        private double radio;

        // Constructor para inicializar el radio
        public Circulo(double radio)
        {
            this.radio = radio;
        }

        // Implementación del método para calcular el área del círculo
        public override double CalcularArea()
        {
            return Math.PI * Math.Pow(radio, 2);
        }

        // Implementación del método para calcular el perímetro del círculo
        public override double CalcularPerimetro()
        {
            return 2 * Math.PI * radio;
        }
    }

    // Clase derivada de Figura para representar un cuadrado
    public class Cuadrado : Figura
    {
        // Lado del cuadrado
        private double lado;

        // Constructor para inicializar el lado
        public Cuadrado(double lado)
        {
            this.lado = lado;
        }

        // Implementación del método para calcular el área del cuadrado
        public override double CalcularArea()
        {
            return lado * lado;
        }

        // Implementación del método para calcular el perímetro del cuadrado
        public override double CalcularPerimetro()
        {
            return 4 * lado;
        }
    }
}