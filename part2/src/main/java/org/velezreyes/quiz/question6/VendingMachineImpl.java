package org.velezreyes.quiz.question6;

import java.util.ArrayList;
import java.util.List;

/**
 * VendingMachineImpl implements the VendingMachine interface and provides vending machine functionality.
 */
public class VendingMachineImpl implements VendingMachine {
    private static VendingMachine instance = new VendingMachineImpl();

    /**
     * Get the singleton instance of the VendingMachine.
     *
     * @return The VendingMachine instance.
     */
    public static VendingMachine getInstance() {
        return instance;
    }

    private int cents;

    @Override
    public void insertQuarter() {
        // Insert a quarter (25 cents) into the vending machine.
        cents += 25;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        // Get a Drink object by name from the vending machine.
        Drink drink = getDrinkByName(name);

        if (drink.getName() == null) {
            // If the drink name is not found, throw an UnknownDrinkException.
            throw new UnknownDrinkException();
        }

        if (drink.getPrice() > cents) {
            // If there's not enough money to buy the selected drink, throw a NotEnoughMoneyException.
            throw new NotEnoughMoneyException();
        }

        // Deduct the drink price from available cents.
        cents -= drink.getPrice();

        return drink;
    }

    private Drink getDrinkByName(String name) {
        // Create a list of available drinks in the vending machine.
        List<Drink> drinkList = new ArrayList<>();
        drinkList.add(new Drink("KarenTea", false, 100));
        drinkList.add(new Drink("ScottCola", true, 75));

        Drink drinkToReturn = new Drink();

        // Iterate through the list to find the drink with the matching name.
        for (Drink drink : drinkList) {
            if (drink.getName().equals(name)) {
                return drink;
            }
        }

        return drinkToReturn;
    }
}
