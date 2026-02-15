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
                a,b=cmd[7:-1].split("=", 1)
                globals()[a]=b
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
    else:
        raise TypeError("Invalid command! Use variables_plus(clear()), variables_plus(create()) or variables_plus(delete()). You can also shorten 'variables_plus' to 'vp'.")
vp=variables_plus
