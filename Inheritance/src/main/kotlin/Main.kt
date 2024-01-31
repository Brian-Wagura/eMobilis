// Inheritance to create a class that is based on another class.
// The class that is being inherited from is called the superclass or
// parent class, and the class that inherits from it is called the subclass
// or child class.


// Parent Class
open class Vehicle(val brand: String, val year: Int) {
    fun start() {
        println("The $brand vehicle has started ....")
    }
}

// Child class inheriting from Vehicle parent
class Car(brand: String, year: Int, val model: String) : Vehicle(brand, year) {
    fun drive() {
        println("The $brand $model is now being driven around.....")
    }
}

fun main() {
//     Creating an instance of the Car class
    val myCar = Car("Honda", 2022, "CRV")

//    Accessing properties and methods from the parent class
    println("Brand: ${myCar.brand}, Year: ${myCar.year}, Model: ${myCar.model}")

//    Accessing method from parent class
    myCar.start()

//    Accessing method from child class
    myCar.drive()
}