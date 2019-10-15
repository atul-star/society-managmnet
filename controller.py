from model import *
from flask import request,render_template


@app.route('/landing/page/')
def landing_page():
    return render_template('main.html')

@app.route('/login/', methods=['POST'])
def login():
    email1=request.form['email']
    #print(email1)
    password1=int(request.form['password'])

    #dbemail=Login.query.filter_by(Email=email1)
    id=Login.query.filter_by(id=password1).first()
    print(id)
    print(type(id))
    #x=int(id)
    # print(type(x))
    all=Login.query.all()
    #print(all)
    #print(id)
    # x=dball.id
    if id:
        msg1='Login successfull'
        return render_template('Home.html',prop=dummp_prop(),properties=Property.query.all(),msg=msg1)

    else:
        msg1="wrong information"
    return render_template('main.html',msg=msg1)
@app.route('/property/welcome/',methods=['GET'])
def property_welcome_page():
    return render_template('Home.html',prop=dummp_prop(),properties=Property.query.all())

def dummp_prop():
    return Property(Pid=0,PName="",PAddress="",PLandmark="",PCity="",PState="",PCounrty="",PZip_Code=0,
               Poc="",PEmail="",PMobile_No="",PTel_No="",PWebsite="",Payment_Portal="")

@app.route('/property/save/',methods=['POST'])
def save_property():
    Pid=int(request.form['pid'])
    if Pid==0:
        p=Property(PName=request.form['pname'],
                   PAddress=request.form['paddress'],
                   PLandmark=request.form['plandmark'],
                   PCity=request.form['pcity'],
                   PState=request.form['pstate'],
                   PCounrty=request.form['pcountry'],
                   PZip_Code=request.form['pzip'],
                   Poc=request.form['ppoc'],
                   PEmail=request.form['pemail'],
                   PMobile_No=request.form['pmobile'],
                   PTel_No=request.form['ptel'],
                   PWebsite=request.form['pwebsite'],
                   Payment_Portal=request.form['ppayment'])
                   # PIs_Active=request.form['pactive']
        db.session.add(p)
        db.session.commit()
        msg = "Property added successfully"
    else:
        prop = Property.query.filter_by(Pid=Pid).first()
        prop.PName = request.form['pname'],
        prop.PAddress = request.form['paddress'],
        prop.PLandmark = request.form['plandmark'],
        prop.PCity = request.form['pcity'],
        prop.PState = request.form['pstate'],
        prop.PCounrty = request.form['pcountry'],
        prop.PZip_Code = request.form['pzip'],
        prop.Poc = request.form['ppoc'],
        prop.PEmail = request.form['pemail'],
        prop.PMobile_No = request.form['pmobile'],
        prop.PTel_No = request.form['ptel'],
        prop.PWebsite = request.form['pwebsite'],
        prop.Payment_Portal = request.form['ppayment']
        # prop.PIs_Active = request.form['pactive']
        db.session.commit()
        print(prop)
        msg = "Property updated successfully............!"
    return render_template('Home.html', properties=Property.query.all(), pmsg=msg, prop=dummp_prop())

@app.route('/property/edit/<int:pid>')
def edit_property(pid):
    property = Property.query.filter_by(Pid=pid).first()
    return render_template('Home.html',properties=Property.query.all(),prop=property)

@app.route('/property/delete/<int:pid>')
def delete_property(pid):
    prop1=Property.query.filter_by(Pid=pid).first()
    db.session.delete(prop1)
    db.session.commit()
    msg="Property deleted successfully........!"
    return render_template('Home.html',prop=dummp_prop(),pmsg=msg,properties=Property.query.all())
#---------------------unit_types  controller------------->

#not integreted yet
#---------------------tenant controller------------->


def dummy_tenant():
    return Tenant(id =0,name = '',uid =0,is_owner = '',lease= '',fromandto='',MOVE_IN =  '',
                  MOVE_OUT = '',status = '',roomates = 0,mobile = '',documents = '',reference = '',
                  email = '',rent = 0.0,LEASE_SIGN_DATE = '',address = '',pan_card ='',aadhar_card='')

@app.route("/resident/welcome/",methods=["GET"])
def resident_welcome():
    return render_template('tenant.html',tenantob=dummy_tenant(),
                                        tenant=Tenant.query.all(),
                                        unit1=Unit.query.all())

@app.route("/resident/save/",methods=["POST"])
def save_info():
    ten = int(request.form['tid'])
    ten1 = int(request.form['uid'])
    print(ten1)
    if ten == 0:
        tenant = Tenant(
                        name=request.form['tname'],
                        uid=request.form['uid'],
                        is_owner=request.form['tisowner'],
                        lease=request.form['tlease'],
                        fromandto=request.form['tfromandto'],
                        #MOVE_IN=request.form['tmovein'],
                        #MOVE_OUT=request.form['tmoveout'],
                        status=request.form['tstatus'],
                        roomates=request.form['troomates'],
                        mobile=request.form['tmobile'],
                        documents=request.form['tdocuments'],
                        reference=request.form['treference'],
                        email=request.form['temail'],
                        rent=request.form['trent'],
                        #LEASE_SIGN_DATE=request.form['tleasesigndate'],
                        address=request.form['taddress'],
                        pan_card=request.form['tpancard'],
                        aadhar_card=request.form['taadharcard'])

        db.session.add(tenant)
        db.session.commit()
        msg = "address Record Saved..!"

    else:
        tanentinstance = Tenant.query.filter_by(id=ten).first()
        tanentinstance.name = request.form['tname']
        tanentinstance.uid = request.form['tunitno']
        tanentinstance.is_owner = request.form['tisowner']
        tanentinstance.lease = request.form['tlease']
        tanentinstance.fromandto = request.form['tfromandto']
        # tanentinstance.MOVE_IN=request.form['tmovein']
        # tanentinstance.MOVE_OUT=request.form['tmoveout']
        tanentinstance.status = request.form['tstatus']
        tanentinstance.roomates = request.form['troomates']
        tanentinstance.mobile = request.form['tmobile']
        tanentinstance.documents = request.form['tdocuments']
        tanentinstance.reference = request.form['treference']
        tanentinstance.email = request.form['temail']
        tanentinstance.rent = request.form['trent']
        # tanentinstance.LEASE_SIGN_DATE=request.form['tleasesigndate']
        tanentinstance.address = request.form['taddress']
        tanentinstance.pan_card = request.form['tpancard']
        tanentinstance.aadhar_card = request.form['taadharcard']
        db.session.commit()
        msg = "Address Updated successfully...."

    return render_template('tenant.html', tenantob=dummy_tenant(),
                           tenant=Tenant.query.all(),
                           unit1=Unit.query.all(),
                           tmsg=msg)

@app.route("/resident/edit/<int:tid>")
def edit_info(tid):
    tanentinstance = Tenant.query.filter_by(id=tid).first()
    print(tanentinstance)
    return render_template('tenant.html',
                           tenantob=tanentinstance,
                           tenant=Tenant.query.all())
                           #unit1=Unit.query.all())
@app.route("/resident/delete/<int:tid>")
def delete_info(tid):
    tanentinstance = Tenant.query.filter_by(id=tid).first()
    if tanentinstance:
        db.session.delete(tanentinstance)
        db.session.commit()
        msg="deleted"
    #print(tanentinstance)
    return render_template('tenant.html',
                           tenantob=tanentinstance,
                           tenant=Tenant.query.all(),tmsg=msg)



if __name__ == '__main__':
    app.run(debug=True)