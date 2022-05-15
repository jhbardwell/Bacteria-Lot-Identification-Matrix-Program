import Tkinter

class AutocompleteEntry(Tkinter.Entry):

        def set_completion_list(self, completion_list):
                self._completion_list = completion_list
                self._hits = []
                self._hit_index = 0
                self.position = 0
                self.bind('<KeyRelease>', self.handle_keyrelease)               

        def autocomplete(self, delta=0):
                if delta: # need to delete selection otherwise we would fix the current position
                        self.delete(self.position, Tkinter.END)
                else: # set position to end so selection starts where textentry ended
                        self.position = len(self.get())
                # collect hits
                _hits = []
                for element in self._completion_list:
                        if element.startswith(self.get().lower()):
                                _hits.append(element)
                # if we have a new hit list, keep this in mind
                if _hits != self._hits:
                        self._hit_index = 0
                        self._hits=_hits
                # only allow cycling if we are in a known hit list
                if _hits == self._hits and self._hits:
                        self._hit_index = (self._hit_index + delta) % len(self._hits)
                # now finally perform the auto completion
                if self._hits:
                        self.delete(0,Tkinter.END)
                        self.insert(0,self._hits[self._hit_index])
                        self.select_range(self.position,Tkinter.END)
                        
        def handle_keyrelease(self, event):
                if len(event.keysym) == 1:
                        self.autocomplete()

def test(test_list):
        """Run a mini application to test the AutocompleteEntry Widget."""
        root = Tkinter.Tk(className=' AutocompleteEntry demo')
        entry = AutocompleteEntry(root)
        entry.set_completion_list(test_list)
        entry.pack()
        entry.focus_set()
        root.mainloop()

if __name__ == '__main__':
        test_list = ('test', 'type', 'true', 'tree')
        test(test_list)


