package org.velezreyes.quiz.question6;

public class VendingMachineImpl implements VendingMachine {

  private Double quarters = 0.0;

  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }

  private void payForDrink(Double payment){
    this.quarters -= payment;
  }

  @Override
  public void insertQuarter() {
    this.quarters += 25.0;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    Drink selectedDrink;

    try {
      selectedDrink = DrinkImpl.valueOf(name);
    } catch (IllegalArgumentException ie){
      throw new UnknownDrinkException();
    }

    if (!(this.quarters >= selectedDrink.price())) {
      throw new NotEnoughMoneyException();
    }

    payForDrink(selectedDrink.price());
    return selectedDrink;
  }
}
