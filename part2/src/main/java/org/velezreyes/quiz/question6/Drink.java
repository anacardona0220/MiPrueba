package org.velezreyes.quiz.question6;

public class Drink {
	
	private String name;
	private boolean isFizzy;
	private int price;
	
	public Drink(String name, boolean isFizzy, int price) {
		super();
		this.name = name;
		this.isFizzy = isFizzy;
		this.price = price;
	}
	
	public Drink() {
	}

	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public boolean isFizzy() {
		return isFizzy;
	}
	public void setFizzy(boolean isFizzy) {
		this.isFizzy = isFizzy;
	}
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		this.price = price;
	}
}
