import sys
from modelo.declarative_base import session, Base, engine
import vista.interfaz_coleccion as ic

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session.close()
    
    app = ic.App(sys.argv)
    sys.exit(app.exec_())
