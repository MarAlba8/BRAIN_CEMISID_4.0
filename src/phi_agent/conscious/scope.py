from phi_agent.conscious.utils import DescriptorQueue, MaxItemsError


class Scope(DescriptorQueue):
    def __init__(self, state: str):
        super().__init__()
        self.state = state

    def has_thought(self, thought: str):
        return self.has_key(key=thought)

    def add_new_thought(self, thought: str):
        try:
            self.enqueue(key=thought)
        except MaxItemsError:
            self.dequeue()
            self.enqueue(key=thought)

    def get_next_thought(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.key
        elif self.head:
            self.current = self.head
            return self.current.key
        return None

    def see_thoughts_in_scope(self):
        print(self.get_keys())

    def get_current_thoughts(self):
        return self.get_keys()
