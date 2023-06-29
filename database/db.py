from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config_reader import config
from models import Base


engine = create_engine(config.db)
Session = sessionmaker(engine)


# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
