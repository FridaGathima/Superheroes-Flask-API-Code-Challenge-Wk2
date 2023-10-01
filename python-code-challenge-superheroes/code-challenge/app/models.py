from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'heros'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    powers = db.relationship("Power", secondary = "hero_powers", back_populates = "heros")

    def __str__(self):
        return self.name
    
class Hero_Power(db.Model):
    __tablename__ = "hero_powers"

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))
    hero_id = db.Column(db.Integer, db.ForeignKey("heros.id"))

    # @validates('strength')
    # def validate_strength(self, key, strength):
    #     if strength == 'Strong' or strength == 'Weak' or strength == 'Average':
    #         raise ValueError ('Strength must either be Strong or Weak or Average')
    #     return strength

    def __str__(self):
        return self.power_id
 
class Power(db.Model):
    __tablename__ = "powers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String, nullable = False)
    heros = db.relationship("Hero", secondary = "hero_powers", back_populates="powers")

    # @validates('name')
    # def validate_name(self, key, name):
    #     if not name:
    #         raise ValueError("Strength must be Present")
    #     return name
        
    # @validates('name')
    # def validate_name(self, key, name):
    #     if name.length < 20:
    #         raise ValueError ("Must have a description more than 50 words in length")
    #     return name

    def __str__(self):
        return self.name
    


        
