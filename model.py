from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
import datetime
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Google@march15@localhost/prop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Property(db.Model):
    Pid = db.Column('id', db.Integer, primary_key=True)
    PName = db.Column('pname', db.String(100), nullable=False, unique=True)
    PAddress = db.Column('paddress', db.String(100), nullable=False)
    PLandmark = db.Column('plandmark', db.String(100), nullable=False)
    PCity = db.Column('pcity', db.String(100), nullable=False)
    PState = db.Column('pstate', db.String(100), nullable=False)
    PCounrty = db.Column('pcounrty', db.String(100), nullable=False)
    PZip_Code = db.Column('pin', db.Integer)
    Poc = db.Column('poc', db.String(100), nullable=False)
    PEmail = db.Column('email', db.String(100), nullable=False)
    PMobile_No = db.Column('mobile', db.String(100), nullable=False)
    PTel_No = db.Column('tel_no', db.String(100), nullable=False)
    PWebsite = db.Column('website', db.String(100), nullable=False)
    Payment_Portal = db.Column('payment', db.String(100), nullable=False)
    created_on = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_on = db.Column(DateTime(timezone=True), onupdate=func.now())


class Login(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    Email = db.Column('email', db.String(80))

    def __str__(self):
        return '{}'.format(self.id)

class Unit_Types(db.Model):
    UT_id = db.Column('ut_id', db.Integer, primary_key=True)
    area = db.Column('UT_Area', db.Integer, nullable=False)
    name = db.Column('UT_Name', db.String(80), unique=True)
    desc = db.Column('UT_Descr', db.String(80), nullable=False)
    created_on = db.Column(DateTime(timezone=True), server_default=func.now())
    # created_by = db.Column( 'Creater_Name',db.String(80))
    updated_on = db.Column(DateTime(timezone=True), onupdate=func.now())
    # updated_by = db.Column( 'Updater_Name',db.String(80))
    pid = db.Column('Pid', db.Integer,
                    db.ForeignKey('property.id'),
                    nullable=True)
    # unit = db.relationship('Unit', backref='unit_types', lazy=False, uselist=True)

    def __str__(self):
        if self.__dict__.__contains__('_sa_instance_state'):
            self.__dict__.pop('_sa_instance_state')
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)



class Unit(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    udesc = db.Column('UNIT_DESCRI', db.String(80), nullable=False)
    tenant = db.relationship('Tenant', backref='unit', lazy=False, uselist=True)
    # unit_types = db.Column('ut_id', db.Integer,
    #                 db.ForeignKey('unit_types.UT_id'),
    #                 nullable=True)
    def __str__(self):
        return 'unit_id={},' \
               'unit_name={}'.format(self.id,self.udesc)

    def __repr__(self):
        return str(self)


class Tenant(db.Model):
    __tablename__ = 'TENANT_INFO'
    id = db.Column('TENANT_ID',db.Integer, primary_key=True)
    name = db.Column('TENANT_NAME', db.String(80), nullable=False)
    #unit_no = db.Column('TENANT UNIT_NO', db.Integer,db.ForeignKey('unit.id'),nullable=True)
    is_owner = db.Column('TENANT_IS_OWNER', db.String(80), nullable=False)
    lease= db.Column('TENANT_LEASE', db.String(80), nullable=False)
    fromandto= db.Column('TENANT_FROMANDTO', db.String(80), nullable=False)
    MOVE_IN =  db.Column(DateTime(timezone=True), server_default=func.now())
    MOVE_OUT = db.Column(DateTime(timezone=True), onupdate=func.now())
    status = db.Column('TENANT_STATUS', db.String(80), nullable=False)
    roomates = db.Column('TENANT_ROOMATES', db.Integer, nullable=False)
    mobile = db.Column('TENANT_MOBILE_NO', db.String(80), nullable=False)
    documents = db.Column('TENANT_DOCUMENTS', db.String(80), nullable=False)
    reference = db.Column('TENANT_REFERENCE', db.String(80), nullable=False)
    email = db.Column('TENANT_EMAIL', db.String(80), nullable=False)
    rent = db.Column('TENANT_RENT', db.Float, nullable=False)
    LEASE_SIGN_DATE = db.Column(DateTime(timezone=True), server_default=func.now())
    address = db.Column('TENANT_ADDRESS', db.String(120), nullable=False)
    pan_card = db.Column('TENANT_PAN_NO', db.String(100), nullable=False)
    aadhar_card = db.Column('TENANT_AADHAR_NO', db.String(100), nullable=False)
    uid = db.Column('unit_id', db.Integer, db.ForeignKey('unit.id'), nullable=True)

if __name__ == '__main__':
    # db.create_all()
    l = Login(Email="email@prop.com", id=12345)
    db.session.add(l)
    db.session.commit()
    #
    # u1=Unit(id=104,udesc='rrrr is avl')
    # u2 = Unit(id=105, udesc='sssss is avl')
    # u3 = Unit(id=106, udesc='yyyyy is avl')
    # db.session.add_all([u1,u2,u3])
    # db.session.commit()
