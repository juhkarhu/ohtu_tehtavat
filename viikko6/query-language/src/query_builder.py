from matchers import And, Or, All, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
  def __init__(self, matchers = And()):
    self.matchers = matchers

  def build(self):
    return self.matchers

  def playsIn(self, team):
    return QueryBuilder(PlaysIn(team))

  def hasAtLeast(self, value, attr):
    return QueryBuilder(And(self.matchers, HasAtLeast(value, attr)))

  def hasFewerThan(self, value, attr):
    return QueryBuilder(And(self.matchers, HasFewerThan(value, attr)))

  def oneOf(self, matcher1, matcher2):
    return QueryBuilder(Or(matcher1, matcher2))