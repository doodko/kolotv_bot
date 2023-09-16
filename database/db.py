from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config_reader import config

engine = create_engine(config.db)
Session = sessionmaker(engine)
