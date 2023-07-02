from flask import Flask, render_template, request, redirect, url_for, session
from Forms import CreateUserForm, LoginUserForm, LoginAdminForm, CreateCustomerOrderForm, CreateUserOrderForm
import shelve
import User, CustomerOrder, UserOrder
from admin import Admin

app = Flask(__name__, static_folder='templates/images')

# example admin
admin = Admin('John', 'Brown', 'q@q', 12345678, 'asdf', '')
db = shelve.open('admin.db', 'c')
try:
    users_dict = db['Admin']
except:
    print("Error in retrieving Users from admin.db.")

db['Users'] = admin


@app.route('/')
def home():
    return render_template('homepage.html')


@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')
        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        for key in users_dict:
            if create_user_form == key:
                error = 'email is already in use'
                return render_template('createUser.html', form=create_user_form, error=error)

        user = User.User(create_user_form.first_name.data, create_user_form.last_name.data,
                         create_user_form.gender.data, create_user_form.date_of_birth.data,
                         create_user_form.date_joined.data, create_user_form.email.data,
                         create_user_form.phone.data, create_user_form.address.data,
                         create_user_form.password.data, create_user_form.remarks.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict
        return redirect(url_for('retrieve_users'))
    return render_template('createUser.html', form=create_user_form)


@app.route('/retrieveUsers')
def retrieve_users():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()
    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)
    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)


@app.route('/deleteUser/<id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']
    users_dict.pop(id)
    db['Users'] = users_dict
    for key in users_dict:
        user = users_dict.get(key)
        userid = user.get_user_id()
    db.close()
    return redirect(url_for('retrieve_users'))


@app.route('/updateUser/<id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']
        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_date_of_birth(update_user_form.date_of_birth.data)
        user.set_date_joined(update_user_form.date_joined.data)
        user.set_email(update_user_form.email.data)
        user.set_phone(update_user_form.phone.data)
        user.set_address(update_user_form.address.data)
        user.set_password(update_user_form.password.data)
        db['Users'] = users_dict
        db.close()
        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()
        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.date_of_birth.data = user.get_date_of_birth()
        update_user_form.date_joined.data = user.get_date_joined()
        update_user_form.email.data = user.get_email()
        update_user_form.phone.data = user.get_phone()
        update_user_form.address.data = user.get_address()
        update_user_form.password.data = user.get_password()
        return render_template('updateUser.html', form=update_user_form)


@app.route('/loginUser', methods=['GET', 'POST'])
def login_user():
    login_user_form = LoginUserForm(request.form)
    if request.method == 'POST' and login_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()
        users_list = []
        for key in users_dict:
            user = users_dict.get(key)
            users_list.append(user)

        valid = False

        for id in users_list:
            if login_user_form.email.data == id.get_email() and login_user_form.password.data == id.get_password():
                valid = True

        if valid is False:
            error = 'email or password is wrong'
            return render_template('loginUser.html', form=login_user_form, error=error)
        else:
            user = session[users_dict[login_user_form.email.data]]

        return render_template('homepage.html')
    return render_template('loginUser.html', form=login_user_form)


@app.route('/loginAdmin', methods=['GET', 'POST'])
def login_admin():
    login_admin_form = LoginAdminForm(request.form)
    if request.method == 'POST' and login_admin_form.validate():
        admin_dict = {}
        db = shelve.open('admin.db', 'r')
        admin_dict = db['Admins']
        db.close()
        admin_list = []
        for key in admin_dict:
            admin = admin_dict.get(key)
            admin_list.append(admin)

        valid = False

        for id in admin_list:
            if login_admin_form.email.data == id.get_email() and login_admin_form.password.data == id.get_password():
                valid = True

        if valid is False:
            error = 'email or password is wrong'
            return render_template('loginAdmin.html', form=login_admin_form, error=error)
        else:
            admin = session[admin_dict[login_admin_form.email.data]]

        return render_template('homepage.html')
    return render_template('loginUser.html', form=login_admin_form)


@app.route('/createCustomerOrder', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerOrderForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        customer = CustomerOrder.Customer(create_customer_form.user_name.data, create_customer_form.name_of_item.data,
                                          create_customer_form.price.data, create_customer_form.no_of_items.data,
                                          create_customer_form.email.data,
                                          create_customer_form.collection.data,
                                          create_customer_form.address.data,create_customer_form.total_price.data)
        customers_dict[customer.get_order_id()] = customer
        db['Customers'] = customers_dict

        db.close()

        return redirect(url_for('retrieve_customers'))
    return render_template('createCustomerOrder.html', form=create_customer_form)


@app.route('/retrieveCustomerOrder')
def retrieve_customers():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()
    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)
    return render_template('retrieveCustomerOrder.html', count=len(customers_list), customers_list=customers_list)


@app.route('/updateCustomerOrder/<int:id>/', methods=['GET', 'POST'])
def update_customer(id):
    update_customer_form = CreateCustomerOrderForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_user_name(update_customer_form.user_name.data)
        customer.set_name_of_item(update_customer_form.name_of_item.data)
        customer.set_price(update_customer_form.price.data)
        customer.set_no_of_items(update_customer_form.no_of_items.data)
        customer.set_email(update_customer_form.email.data)
        customer.set_collection(update_customer_form.collection.data)
        customer.set_address(update_customer_form.address.data)
        customer.set_total_price(update_customer_form.total_price.data)

        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('retrieve_customers'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.user_name.data = customer.get_user_name()
        update_customer_form.name_of_item.data = customer.get_name_of_item()
        update_customer_form.price.data = customer.get_price()
        update_customer_form.no_of_items.data = customer.get_no_of_items()
        update_customer_form.email.data = customer.get_email()
        update_customer_form.collection.date = customer.get_collection()
        update_customer_form.address.data = customer.get_address()
        update_customer_form.total_price.data = customer.get_total_price()

        return render_template('updateCustomerOrder.html', form=update_customer_form)


@app.route('/deleteCustomerOrder/<int:id>', methods=['POST'])
def delete_customer(id):
    customers_dict = {}
    db = shelve.open('customer.db', 'w')
    customers_dict = db['Customers']
    customers_dict.pop(id)

    db['Customers'] = customers_dict
    db.close()

    return redirect(url_for('retrieve_customers'))


@app.route('/createUserOrder', methods=['GET', 'POST'])
def create_user_order():
    create_user_order_form = CreateUserOrderForm(request.form)
    if request.method == 'POST' and create_user_order_form.validate():
        user_orders_dict = {}
        db = shelve.open('userorder.db', 'c')

        try:
            user_orders_dict = db['UserOrder']
        except:
            print("Error in retrieving Users from userorder.db.")

        userorder = UserOrder.UserOrder(create_user_order_form.name_of_item.data,
                                        create_user_order_form.price.data, create_user_order_form.no_of_items.data,
                                        create_user_order_form.collection.data,create_user_order_form.address.data,
                                        create_user_order_form.total_price.data)

        user_orders_dict[userorder.get_user_order_id()] = userorder
        db['UserOrder'] = user_orders_dict

        db.close()

        return redirect(url_for('retrieve_user_order'))
    return render_template('createUserOrder.html', form=create_user_order_form)


@app.route('/retrieveUserOrder')
def retrieve_user_order():
    user_orders_dict = {}
    db = shelve.open('userorder.db', 'r')
    user_orders_dict = db['UserOrder']
    db.close()

    user_orders_list = []
    for key in user_orders_dict:
        userorder = user_orders_dict.get(key)
        user_orders_list.append(userorder)

    return render_template('retrieveUserOrder.html', count=len(user_orders_list), user_orders_list=user_orders_list)


@app.route('/updateUserOrder/<int:id>/', methods=['GET', 'POST'])
def update_user_order(id):
    update_user_order_form = CreateUserOrderForm(request.form)
    if request.method == 'POST' and update_user_order_form.validate():
        user_orders_dict = {}
        db = shelve.open('userorder.db', 'w')
        user_orders_dict = db['UserOrder']

        userorder = user_orders_dict.get(id)
        userorder.set_name_of_item(update_user_order_form.name_of_item.data)
        userorder.set_price(update_user_order_form.price.data)
        userorder.set_no_of_items(update_user_order_form.no_of_items.data)
        userorder.set_collection(update_user_order_form.collection.data)
        userorder.set_address(update_user_order_form.address.data)
        userorder.set_total_price(update_user_order_form.total_price.data)

        db['UserOrder'] = user_orders_dict
        db.close()

        return redirect(url_for('retrieve_user_order'))
    else:
        user_orders_dict = {}
        db = shelve.open('userorder.db', 'r')
        user_orders_dict = db['UserOrder']
        db.close()

        userorder = user_orders_dict.get(id)
        update_user_order_form.name_of_item.data = userorder.get_name_of_item()
        update_user_order_form.price.data = userorder.get_price()
        update_user_order_form.no_of_items.data = userorder.get_no_of_items()
        update_user_order_form.collection.data = userorder.get_collection()
        update_user_order_form.address.data = userorder.get_address()
        update_user_order_form.total_price.data = userorder.get_total_price()

        return render_template('updateUserOrder.html', form=update_user_order_form)


@app.route('/deleteUserOrder/<int:id>', methods=['POST'])
def delete_user_order(id):
    user_orders_dict = {}
    db = shelve.open('userorder.db', 'w')
    user_orders_dict = db['UserOrder']
    user_orders_dict.pop(id)

    db['UserOrder'] = user_orders_dict
    db.close()

    return redirect(url_for('retrieve_user_order'))


@app.route('/men')
def men():
    return render_template('men.html')

@app.route('/women')
def women():
    return render_template('women.html')


if __name__ == '__main__':
    app.run()
