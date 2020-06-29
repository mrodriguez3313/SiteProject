from flask import render_template, Blueprint
core = Blueprint('core', __name__)
states_a = ["California", "Texas", "Minnesota"]
states_array = sorted(states_a)


National_orgs_array = []
Other_Resources = [("pbresources.com", "http://www.pb-resources.com"), ("HungryHungryHooker.com",
                                                                        "https://hungryhungryhooker.squarespace.com/blackownedbiz"), ("Adhesive Unity.com", "https://adhesiveunity.com/")]


@core.route('/')
def index():
    return render_template("index.html", states=states_array, other=Other_Resources)


@core.route('/Stateslist')
def State_list():
    return render_template('States_list.html', states=states_array, other=Other_Resources)


@core.route('/NationalDonate')
def donate():
    return render_template('donate.html', title="Donate Nationwide", states=states_array, other=Other_Resources)


@core.route('/NationalOrganizations')
def organize():
    return render_template('organize.html', title="National Organizations", states=states_array, orgs=National_orgs_array, other=Other_Resources)


@core.route('/NationalPetitions')
def petitions():
    return render_template('petitions.html', title="National Petitions", states=states_array, other=Other_Resources)


@core.route('/CampaignZero')
def zero():
    return render_template('campaign.html')


@core.route('/Texas')
def Texas():
    return render_template('state_home_page.html', title="Texas", states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Businesses TX", "core.Tex_biz"), other=Other_Resources)


@core.route('/Texas/donate')
def Texas_donate():
    return render_template('state_donate.html', title="Texas", states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Business TX", "core.Tex_biz"), other=Other_Resources)


@core.route('/Texas/organizations')
def Texas_org():
    return render_template('state_org.html', title="Texas", states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Business TX", "core.Tex_biz"), other=Other_Resources)


@core.route('/Texas/BlackBusiness')
def Tex_biz():
    return render_template('state_biz.html', title="Texas", states=states_array, donation_page=("Donation Pages TX", "core.Texas_donate"), state_orgs=("Organizations TX", "core.Texas_org"), state_black_businesses=("Black Business TX", "core.Tex_biz"), other=Other_Resources)


@core.route('/California')
def Cali():
    return render_template('state_home_page.html', title="California", states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA", "core.Cali_biz"), other=Other_Resources)


@core.route('/California/donate')
def Cali_donate():
    return render_template('state_donate.html', title="California", states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA", "core.Cali_biz"), other=Other_Resources)


@core.route('/California/organizations')
def Cali_org():
    return render_template('state_org.html', title="California", states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA", "core.Cali_biz"), other=Other_Resources)


@core.route('/California/BlackBusiness')
def Cali_biz():
    return render_template('state_biz.html', title="California", states=states_array, donation_page=("Donation Pages CA", "core.Cali_donate"), state_orgs=("Organizations CA", "core.Cali_org"), state_black_businesses=("Black Businesses CA", "core.Cali_biz"), other=Other_Resources)


@core.route('/Minnesota')
def MN():
    return render_template('state_home_page.html', title="Minnesota", states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz"), other=Other_Resources)


@core.route('/Minnesota/donate')
def MN_donate():
    return render_template('state_donate.html', title="Minnesota", states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz"), other=Other_Resources)


@core.route('/Minnesota/organizations')
def MN_org():
    return render_template('state_org.html', title="Minnesota", states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz"), other=Other_Resources)


@core.route('/Minnesota/BlackBusiness')
def MN_biz():
    return render_template('state_biz.html', title="Minnesota", states=states_array, donation_page=("Donation Pages MN", "core.MN_donate"), state_orgs=("Organizations MN", "core.MN_org"), state_black_businesses=("Black Businesses MN", "core.MN_biz"), other=Other_Resources)
