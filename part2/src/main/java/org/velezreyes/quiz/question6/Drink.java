package org.velezreyes.quiz.question6;

/**
 * Drink represents a drink available in a vending machine.
 */
public class Drink {
    private String name;
    private boolean isFizzy;
    private int price;

    /**
     * Creates a Drink object with the provided name, fizziness, and price.
     *
     * @param name     The name of the drink.
     * @param isFizzy  Indicates whether the drink is fizzy.
     * @param price    The price of the drink.
     */
    public Drink(String name, boolean isFizzy, int price) {
        this.name = name;
        this.isFizzy = isFizzy;
        this.price = price;
    }

    /**
     * Default constructor for creating an empty Drink object.
     */
    public Drink() {
    }

    /**
     * Get the name of the drink.
     *
     * @return The name of the drink.
     */
    public String getName() {
        return name;
    }

    /**
     * Set the name of the drink.
     *
     * @param name The name of the drink.
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Check if the drink is fizzy.
     *
     * @return True if the drink is fizzy, false otherwise.
     */
    public boolean isFizzy() {
        return isFizzy;
    }

    /**
     * Set the fizziness of the drink.
     *
     * @param isFizzy Indicates whether the drink is fizzy.
     */
    public void setFizzy(boolean isFizzy) {
        this.isFizzy = isFizzy;
    }

    /**
     * Get the price of the drink.
     *
     * @return The price of the drink.
     */
    public int getPrice() {
        return price;
    }

    /**
     * Set the price of the drink.
     *
     * @param price The price of the drink.
     */
    public void setPrice(int price) {
        this.price = price;
    }
}
