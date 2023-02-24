from datetime import date

class Movie:
    def __init__(self, name, year, duration, director):
        try:
            self.name = name
            self.year = year
            self.duration = duration
            self.director = director        
            self.reviews = []
        except ValueError as err:
            raise

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        try:
            self._year = int(value)
            if int(value) < 1900 or int(value) > date.today().year:
                raise ValueError("Duration must be an integer between 1900 and " \
                    + str(date.today().year)) from None
        except ValueError:
            raise 

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        try:
            self._duration = int(value)
            if int(value) <= 0:
                raise ValueError("Duration must be an integer greater than zero") \
                    from None
        except ValueError:
            raise               

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        self._director = value

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, value):
        self._reviews = value

    def add_review(self, score):
        if score >=0 and score <=5:
            self._reviews.append(score)
        else:
            raise ValueError("invalid review score: " + str(score)) from None

    def get_review_average(self):
        sum = 0
        for i in self._reviews:
            sum = sum + i

        if len(self._reviews) > 0:
            return round(sum / len(self._reviews), 2)
        else:
            return 0

    def get_age(self):
        return date.today().year - self._year

    def __str__(self):
        temp_str = "------------------------------" \
            +"\nMovie info: " \
            +"\nName: " + self._name \
            +"\nRelease Year: " + str(self._year) \
            + "(age: " + str(self.get_age()) + ")" \
            +"\nDuration: " + str(self._duration) \
            +"\nDirector: " + str(self._director) \
            +"\nReviews: " 

        for r in self._reviews:
            temp_str = temp_str + str(r) + " "

        temp_str = temp_str + "\nReviews average: " \
            + str(self.get_review_average()) \
            +"\n------------------------------"
            
        return temp_str

def main():
    m = Movie("The Movie", 2023, 120, "john doe")
    m.duration = 150
    m.add_review(3)
    m.add_review(0)
    m.add_review(4)

    print("Movie age: " + str(m.get_age()))
    print("Review average score: " + str(m.get_review_average()))
    print("Review details:")
    print(m)

if __name__ == "__main__":
    main()