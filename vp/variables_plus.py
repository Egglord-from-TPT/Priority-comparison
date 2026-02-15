def variables_plus(cmd):
    cmd=cmd.strip()
    a=""
    b=""
    if cmd.startswith("clear(") and cmd.endswith(")"):
        if cmd[6:-1] == "":
            for i in globals():
                if not i.startswith("__") and not callable(i) and not i.startswith("<function") and not i:
                    globals()[i]=""
        else:
            try:
                for i in globals():
                    if not i.startswith("__") and not callable(i) and not i.startswith("<function") and not i:
                        if i==cmd[6:-1]:
                            globals()[i]=""
            except Exception:
                raise TypeError("Invalid variable! Enter a variables name or leave it blank to clear the variable(s).")
    elif cmd.startswith("create(") and cmd.endswith(")"):
        if not cmd[7:-1] == "":
            try:
                if "=" in cmd[7:-1]:
                    a,b=cmd[7:-1].split("=", 1)
                    if not a in globals():
                        globals()[a]=b
                    else:
                        raise SyntaxError("Variable "+a+" already exists! Use vp.vp('write()') to modify a variable's contents.")
                else:
                    a=cmd[7:-1]
                    if not a in globals():
                        globals()[a]=""
                    else:
                        raise SyntaxError("Variable "+a+" already exists! Use vp.vp('write()') to modify a variable's contents.")
            except Exception:
                raise TypeError("I don't even know what you did wrong, but you did something wrong.")
        else:
            raise TypeError("You can't create a blank variable.")
    elif cmd.startswith("delete(") and cmd.endswith(")"):
        if not cmd[7:-1] == "":
            for i in globals():
                if not i.startswith("__") and not callable(i):
                    if i==cmd[7:-1]:
                        try:
                            del globals()[i]
                            break
                        except Exception:
                            raise TypeError("Variable", i, "doesn't exist.")
        else:
            raise SyntaxError("You can't delete a blank variable.")
    elif cmd.startswith("read(") and cmd.endswith(")"):
        if cmd[5:-1] in globals():
            return globals()[cmd[5:-1]]
        else:
            raise TypeError("Variable", cmd[5:-1], "doesn't exist.")
    elif cmd.startswith("write(") and cmd.endswith(")"):
        if not cmd[6:-1] == "":
            try:
                if "=" in cmd[6:-1]:
                    a,b=cmd[6:-1].split("=", 1)
                    if a in globals():
                        globals()[a]=b
                    else:
                        raise SyntaxError("Variable "+a+" doesn't exist! Use vp.vp('create()') to create a new variable.")
                else:
                    a=cmd[6:-1]
                    raise SyntaxError("To modify variable "+a+", you must use '=' .")
            except Exception:
                raise TypeError("I don't even know what you did wrong, but you did something wrong.")
        else:
            raise TypeError("You can't modify a blank variable.")
    else:
        raise TypeError("Invalid command! Use vp.vp('clear()'), vp.vp('create()'), vp.vp('write()') or vp.vp('delete()').")
vp=variables_plus
