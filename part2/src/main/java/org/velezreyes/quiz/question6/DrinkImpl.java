package org.velezreyes.quiz.question6;

enum DrinkImpl implements Drink {

    ScottCola {
        @Override
        public String getName() {
            return this.name();
        }

        @Override
        public boolean isFizzy() {
            return true;
        }

        @Override
        public Double price() {
            return 75.0;
        }


    },

    KarenTea {
        @Override
        public String getName() {
            return this.name();
        }

        @Override
        public boolean isFizzy() {
            return false;
        }

        @Override
        public Double price() {
            return 100.0;
        }
    }
}
