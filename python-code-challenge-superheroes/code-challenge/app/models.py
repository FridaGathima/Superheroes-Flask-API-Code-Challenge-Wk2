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
    
class HeroPower(db.Model):
    __tablename__ = "hero_powers"

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    power_id = db.Column(db.Integer, db.ForeignKey("powers.id"))
    hero_id = db.Column(db.Integer, db.ForeignKey("heros.id"))

    # @validates('strength')
    # def validate_strength(self, key, strength):
    #     if strength != 'Strong' or strength != 'Weak' or strength != 'Average':
    #         raise ValueError ('Strength must either be Strong or Weak or Average')
    #     return strength

    # def __str__(self):
    #     return self.power_id
 
class Power(db.Model):
    __tablename__ = "powers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String, nullable = False)
    heros = db.relationship("Hero", secondary = "hero_powers", back_populates="powers")

    # @validates('description')
    # def validate_description(self, key, description):
    #     if not description:
    #         raise ValueError("Strength must be Present")
    #     return description
        
    # @validates('description')
    # def validate_name(self, key, description):
    #     if description.length < 20:
    #         raise ValueError ("Must have a description more than 20 words in length")
    #     return description

    def __str__(self):
        return self.name
    


        
