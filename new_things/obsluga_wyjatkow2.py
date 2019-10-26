try:
    raise Exception("Dzwon po Policje")
except Exception:
    print("Tutaj sie jeszcze nie wywalilem.")
raise Exception("inny error")