package org.velezreyes.quiz.question6;

import java.util.List;
import java.util.ArrayList;

public class VendingMachineImpl {
	public static VendingMachine getInstance() {
	    return new MyVendingMachine();
	}
	
	private static class MyVendingMachine implements VendingMachine {
		
		private int cents;

        @Override
        public void insertQuarter() {
        	cents = cents + 25;
        }

        @Override
        public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        	Drink drink = getDrinkByName(name);
        	
        	//Checking if the drink name returned from getDrinkByName method, is equal to the parameter 'name'
        	if (drink.getName() == null) {
        		throw new UnknownDrinkException();
        	}
        	
        	//Checking if the price is higher than the cents introduced in the vending machine
        	if (drink.getPrice() > cents) {
        		throw new NotEnoughMoneyException();
        	}
        	
        	//If there is no failure, I mean, if the name is correct, and the money is enough to buy the drink, 
        	//then the drink found in the getDrinkByName method is returned
        	
            return drink;
        }

		private Drink getDrinkByName(String name) {
			// This is replacing the call to a database
			List<Drink> drinkList = new ArrayList<>();
			drinkList.add(new Drink("KarenTea", false, 100));
			drinkList.add(new Drink("ScottCola", true, 75));
			
			Drink drinkToReturn = new Drink();
			
			//Searching the name of the drink, inside the list of drinks created above. If the name is found in the list, 
			//the drink is returned, else, an empty drink object is returned.
			for (Drink drink : drinkList) {
				if (drink.getName().equals(name)) {
					return drink;
				}
			}
			return drinkToReturn;
		}
    }
}

