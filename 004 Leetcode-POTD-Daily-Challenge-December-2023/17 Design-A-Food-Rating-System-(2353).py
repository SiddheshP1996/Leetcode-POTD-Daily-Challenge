from sortedcontainers import SortedList


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.infoOfFood = {}
        self.sortTheCuisine = defaultdict(SortedList)

        for foodAvailable, cuisinePresent, ratingOfFood in zip(foods, cuisines, ratings):
            self.infoOfFood[foodAvailable] = (cuisinePresent, ratingOfFood)
            self.sortTheCuisine[cuisinePresent].add((-ratingOfFood, foodAvailable))

    def changeRating(self, foodAvailable: str, newRatingOfFood: int) -> None:
        cuisinePresent, oldRatingOfFood = self.infoOfFood[foodAvailable]
        self.infoOfFood[foodAvailable] = (cuisinePresent, newRatingOfFood)
        self.sortTheCuisine[cuisinePresent].discard((-oldRatingOfFood, foodAvailable))
        self.sortTheCuisine[cuisinePresent].add((-newRatingOfFood, foodAvailable))

    def highestRated(self, cuisinePresent: str) -> str:
        return self.sortTheCuisine[cuisinePresent][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
