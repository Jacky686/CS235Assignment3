
class Actor:

    def __init__(self, actor_full_name: str, actor_colleagues=None):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

        if actor_colleagues is None:
            self.__actor_colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @actor_full_name.setter
    def actor_full_name(self, full_name: str):
        if isinstance(full_name, str):
            self.__actor_full_name = full_name.strip()

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if self.__actor_full_name == other.actor_full_name:
            return True

        return False

    def __lt__(self, other):
        if self.__actor_full_name < other.actor_full_name:
            return True

        return False

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__actor_colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__actor_colleagues:
            return True

        return False


class TestActorMethods:

    def test_init(self):
        pass
        # actor1 = Actor("Angelina Jolie")
        # print(actor1)
        # actor2 = Actor("")
        # print(actor2)
        # actor3 = Actor(42)
        # print(actor3)
