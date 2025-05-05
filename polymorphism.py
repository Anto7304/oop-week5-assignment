#Base Animal class
class Animal {
    constructor(name, habitat) {
        this.name = name;
        this.habitat = habitat;
    }

    move() {
        console.log(`${this.name} is moving in some way.`);
    }

    speak() {
        console.log(`${this.name} makes a sound.`);
    }
}

""" Subclass examples with polymorphic move() methods"""
class Bird extends Animal {
    constructor(name, habitat, wingspan) {
        super(name, habitat);
        this.wingspan = wingspan;
    }

    move() {
        console.log(`${this.name} is flying with a ${this.wingspan}cm wingspan! 🕊️`);
    }

    speak() {
        console.log(`${this.name} chirps melodiously! 🎵`);
    }
}

class Fish extends Animal {
    constructor(name, habitat, finType) {
        super(name, habitat);
        this.finType = finType;
    }

    move() {
        console.log(`${this.name} is swimming with its ${this.finType} fins! 🐟`);
    }

    speak() {
        console.log(`${this.name} makes bubble sounds... blub blub! 💦`);
    }
}

class Snake extends Animal {
    constructor(name, habitat, isVenomous) {
        super(name, habitat);
        this.isVenomous = isVenomous;
    }

    move() {
        console.log(`${this.name} is slithering ${this.isVenomous ? 'dangerously' : 'harmlessly'}! 🐍`);
    }

    speak() {
        console.log(`${this.name} hisses ${this.isVenomous ? 'menacingly' : 'softly'}!`);
    }
}

# Demonstration of polymorphism
function demonstrateMovement(animals) {
    console.log("\n--- Polymorphism in Action ---");
    animals.forEach(animal => {
        animal.move(); // Same method call, different behaviors
    });
}

# Create instances
const eagle = new Bird('Golden Eagle', 'Mountains', 200);
const clownfish = new Fish('Nemo', 'Coral Reef', 'pectoral');
const cobra = new Snake('King Cobra', 'Jungle', true);
const python = new Snake('Ball Python', 'Grasslands', false);

# Demonstrate polymorphism
demonstrateMovement([eagle, clownfish, cobra, python]);

# Additional demonstration
console.log("\n--- Speaking Demonstration ---");
[eagle, clownfish, cobra].forEach(animal => animal.speak());