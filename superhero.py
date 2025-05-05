class Superhero {
    constructor(name, alias, powers, universe, secretIdentity) {
        this.name = name;
        this.alias = alias;
        this.powers = powers;
        this.universe = universe;
        this._secretIdentity = secretIdentity; // Encapsulated property
    }

    // Getter for encapsulated property
    get secretIdentity() {
        return this._secretIdentity;
    }

    // Setter for encapsulated property
    set secretIdentity(newIdentity) {
        if (typeof newIdentity === 'string' && newIdentity.length > 0) {
            this._secretIdentity = newIdentity;
        } else {
            console.log("Invalid secret identity!");
        }
    }

    usePower() {
        const randomPower = this.powers[Math.floor(Math.random() * this.powers.length)];
        console.log(`${this.alias} uses ${randomPower}!`);
    }

    assemble() {
        console.log(`${this.alias} has answered the call to assemble!`);
    }

    static createRandomHero() {
        const names = ['Thor', 'Iron Man', 'Black Widow', 'Hulk', 'Captain America'];
        const powers = [
            ['Super strength', 'Lightning control', 'Flight'],
            ['Tech genius', 'Repulsor beams', 'Flight'],
            ['Master spy', 'Martial arts', 'Weapons expert'],
            ['Super strength', 'Invulnerability', 'Rage mode'],
            ['Super strength', 'Shield mastery', 'Leadership']
        ];
        const randomIndex = Math.floor(Math.random() * names.length);
        return new Superhero(
            names[randomIndex],
            names[randomIndex],
            powers[randomIndex],
            'Marvel',
            'Classified'
        );
    }
}

// Inheritance example: Mutant extends Superhero
class Mutant extends Superhero {
    constructor(name, alias, powers, universe, secretIdentity, mutationLevel) {
        super(name, alias, powers, universe, secretIdentity);
        this.mutationLevel = mutationLevel;
    }

    // Override usePower method
    usePower() {
        if (this.mutationLevel > 5) {
            console.log(`${this.alias} unleashes a MUTANT POWER SURGE!`);
            this.powers.forEach(power => console.log(`>>> ${power} <<<`));
        } else {
            super.usePower();
        }
    }

    // New method specific to Mutants
    levelUp() {
        this.mutationLevel += 1;
        console.log(`${this.alias}'s mutation level increased to ${this.mutationLevel}!`);
    }
}

// Usage examples
const spiderMan = new Superhero(
    'Peter Parker',
    'Spider-Man',
    ['Web-slinging', 'Spider-sense', 'Wall-crawling'],
    'Marvel',
    'Peter Parker'
);

const wolverine = new Mutant(
    'James Howlett',
    'Wolverine',
    ['Healing factor', 'Adamantium claws', 'Enhanced senses'],
    'Marvel',
    'Logan',
    7
);

console.log("--- Superhero Class Demo ---");
spiderMan.usePower();
spiderMan.assemble();
console.log(spiderMan.secretIdentity); // Using getter

console.log("\n--- Mutant Class Demo (Inheritance) ---");
wolverine.usePower(); // Different behavior due to polymorphism
wolverine.levelUp();
console.log(wolverine.secretIdentity); // Inherited getter

console.log("\n--- Static Method Demo ---");
const randomHero = Superhero.createRandomHero();
randomHero.usePower();