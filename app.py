from calcul import calculate

class StoryNode:
    def __init__(self, expression: str, res: str | None = None, err: BaseException | None = None):
        if (res == None and err == None) or (res != None and err != None): 
            raise ValueError("Только один из аргументов res или err должен быть None")
        
        self.res = res
        self.expression = expression
        self.err = err

    def __repr__(self):
        if self.res == None: 
            return f"введенное выражение ='{self.expression}', ошибка: {self.err}"
        if self.err == None:
            return f"введенное выражение ='{self.expression}', результат =  {self.res}"
       


class Application:
    def __init__(self):
        self.story = []
        self.exit_flag = True
        self.commands = {
            "story": lambda: print(*self.story, sep="\n"),
            "exit": self.exit_function,
            "help": lambda: print("допустимые символы: \n\t(, ), *, /, +, - \n\n допустимые команды: \n\texit \n\tstory")
        }
   
    def exit_function(self):
        self.exit_flag = False

    def run(self):

        while self.exit_flag:
            calc = None
            err = None
            text = input("введите выражение: ")

            if text in self.commands: 
                self.commands[text]()
                continue
            
            try:
                calc = calculate(text)
                print(calc)        
            except BaseException as e:
                err = e
                print(err)

            story_node = StoryNode(
                text, 
                calc,
                err
            )

            self.story.append(story_node)

   
app = Application()
app.run()

