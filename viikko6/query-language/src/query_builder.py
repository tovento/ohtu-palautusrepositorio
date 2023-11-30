from matchers import All, And, Not, Or, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self, query_object=All()):
        self.query_object = query_object

    def build(self):
        return self.query_object

    def playsIn(self, team):
        return QueryBuilder(And(self.query_object, PlaysIn(team)))

    def hasAtLeast(self, amount, point_type):
        return QueryBuilder(
            And(self.query_object, HasAtLeast(amount, point_type)))

    def hasFewerThan(self, amount, point_type):
        return QueryBuilder(
            And(self.query_object, HasFewerThan(amount, point_type)))
