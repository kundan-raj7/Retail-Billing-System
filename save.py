import tempfile
from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

#functionality part


def clear():
    bathsoapEntry.insert(0, 0)
    FacecreamEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)
    hairsprayEntry.insert(0, 0)
    bodylotionEntry.insert(0, 0)

    FacewashEntry.insert(0, 0)


    daalEntry.insert(0,0)
    wheatEntry.insert(0, 0)
    riceEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    teaEntry.insert(0, 0)
    sugarEntry.insert(0, 0)

    pepsiEntry.insert(0, 0)
    cocacolaEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    dewEntry.insert(0, 0)
    frootiEntry.insert(0, 0)
    maazaEntry.insert(0, 0)

    costmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    colddrinkstaxEntry.delete(0,END)


    costmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    colddrinkspriceEntry.delete(0,END)


    nameEntery.delete(0, END)
    phoneEntery.delete(0, END)
    billnumberEntery.delete(0, END)

    textarea.delete(1.0,END)






def send_email():
    def send_email():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get())
            message=email_textarea.get((1.0,END))

            ob.sendmail(senderEntry.get(),recieverEntry.get())
            ob.quit()
            messagebox.showinfo('success','bill is successfully sent',parent=root1)
            root1.destroy()

        except:
            messagebox.showerror('Error','something went to wrong,please try again',parent=root1)


    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','bill is empty')
    else:

        root1=Toplevel()
        root1.grab_set()
    root1.title('send email')
    root1.config(bg='gray20')
    root1.resizable(0,0)

    senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
    senderFrame.grid(row=0,column=0,padx=40,pady=20)

    senderLabel=Label(senderFrame,text="sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
    senderLabel.grid(row=0,column=0,padx=10,pady=8)


    senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
    senderEntry.grid(row=0,column=1,padx=10,pady=8)

    passwordLabel = Label(senderFrame, text="passsword", font=('arial', 14, 'bold'), bg='gray20', fg='white')
    passwordLabel.grid(row=1, column=0, padx=10, pady=8)

    passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
    passwordEntry.grid(row=1, column=1, padx=10, pady=8)



    recipientFrame=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
    recipientFrame.grid(row=1,column=0,padx=40,pady=20)

    recieverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='gray20', fg='white')
    recieverLabel.grid(row=0, column=0, padx=10, pady=8)


    recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
    recieverEntry.grid(row=0, column=1, padx=10, pady=8)

    messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='gray20', fg='white')
    messageLabel.grid(row=1, column=0, padx=10, pady=8)



    email_textarea=Text(recipientFrame, font=('arial',14, 'bold'),bd=2,relief=SUNKEN,
                        width=42,height=11)

    email_textarea.grid(row=2,column=0,columnspan=2)
    email_textarea.delete(1.0,END)
    email_textarea.insert(END,textarea.grid(1.0,END).replace('=',''))

    sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),command=send_email)
    sendButton.grid(row=2,column=0,pady=20)








def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','bill is empty')
    else:
        file=tempfile.mktemp('txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.statfile(file,'print')




def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntery.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
                f.close()
                break
    else:
        messagebox.showerror('Error','invalid Bill Number')


if not  os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global  billnumber
    result=messagebox.askyesno('confirm','Do you want to save the bill? ')
    if result:
        bill_content=textarea.get(1.0,END)
        open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('success',f'billnumber {billnumber} is save successfully')

billnumber = random.randint(500, 1000)


def bill_area():
    if nameEntery.get()=='' or phoneEntery=='':
       messagebox.showerror('Error' , 'Costomer Detail Are Required')
    elif costmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and costmeticpriceEntry.get()=='':
        messagebox.showerror('Error','No products are selected')
    elif costmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and costmeticpriceEntry.get()=='0 Rs':
        messagebox.showerror('Error', 'No Products are Selected')
    else:



     textarea.delete(1.0, END)

    textarea.insert(END, '\t\t**Welcome Customer**\n')
    textarea.insert(END, f'\nBill Number: {billnumber}\n')
    textarea.insert(END, f'\nCustomer Name: {nameEntery.get()}\n')
    textarea.insert(END, f'\nCustomer Phone Number: {phoneEntery.get()}\n')
    textarea.insert(END, '\n=======================================================')
    textarea.insert(END, 'product\t\t\tQuantity\t\t\tPrice')
    textarea.insert(END, '\n=======================================================')
    if bathsoapEntry.get() != '0':
        textarea.insert(END, f'\nBath soap\t\t\t{bathsoapEntry.get()}\t\t\t{bathsoapprice} Rs')

    if hairsprayEntry.get() != '0':
        textarea.insert(END, f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')

    if hairgelEntry.get() != '0':
        textarea.insert(END, f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')

    if FacecreamEntry.get() != '0':
        textarea.insert(END, f'\nFace Cream\t\t\t{FacecreamEntry.get()}\t\t\t{Facecreamprice} Rs')

    if FacewashEntry.get() != '0':
        textarea.insert(END, f'\nFace Wash\t\t\t{FacewashEntry.get()}\t\t\t{Facewashprice} Rs')

    if bodylotionEntry.get() != '0':
        textarea.insert(END, f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')

    if riceEntry.get() != '0':
        textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
    if daalEntry.get() != '0':
        textarea.insert(END, f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
    if oilEntry.get() != '0':
        textarea.insert(END, f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
    if sugarEntry.get() != '0':
        textarea.insert(END, f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
    if wheatEntry.get() != '0':
        textarea.insert(END, f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')

    if teaEntry.get() != '0':
        textarea.insert(END, f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')

    if maazaEntry.get() != '0':
        textarea.insert(END, f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')

    if frootiEntry.get() != '0':
        textarea.insert(END, f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')

    if pepsiEntry.get() != '0':
        textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')

    if spriteEntry.get() != '0':
        textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')

    if cocacolaEntry.get() != '0':
        textarea.insert(END, f'\nCoca Cola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Rs')

    if dewEntry.get() != '0':
        textarea.insert(END, f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')

    textarea.insert(END, '\n-------------------------------------------------------')

    if costmetictaxEntry.get() != '0.0 Rs':
        textarea.insert(END, f'\nCostmetic Tax\t\t\t\t{costmetictaxEntry.get()}')

    if grocerytaxEntry.get() != '0.0 Rs':
        textarea.insert(END, f'\n Grocery Tax\t\t\t\t{grocerytaxEntry.get()}')

    if colddrinkstaxEntry.get() != '0.0 Rs':
        textarea.insert(END, f'\nDrinks Tax\t\t\t\t{colddrinkstaxEntry.get()}')

    textarea.insert(END, f'\nTotal Bill \t\t\t\t{totalbill}')
    textarea.insert(END,'\n--------------------------------------------------------')
    save_bill()

def total():
    global bathsoapprice, hairsprayprice, hairgelprice, Facecreamprice, Facewashprice, bodylotionprice
    global riceprice, daalprice, oilprice, sugarprice, wheatprice, teaprice
    global frootiprice, dewprice, cocacolaprice, spriteprice, pepsiprice, maazaprice
    global totalbill
    #costmeticprice calculation

    bathsoapprice = int(bathsoapEntry.get()) * 10
    Facecreamprice = int(FacecreamEntry.get()) * 60
    Facewashprice = int(FacewashEntry.get()) * 50
    hairsprayprice = int(hairsprayEntry.get()) * 90
    hairgelprice = int(hairgelEntry.get()) * 30
    bodylotionprice = int(bodylotionEntry.get()) * 40

    totalcostmeticprice = bathsoapprice + Facecreamprice + Facewashprice + hairgelprice + hairsprayprice + bodylotionprice
    costmeticpriceEntry.delete(0, END)
    costmeticpriceEntry.insert(0, f'{totalcostmeticprice} Rs')
    costmetictax = totalcostmeticprice * 0.12
    costmetictaxEntry.delete(0, END)
    costmetictaxEntry.insert(0, str(costmetictax) + 'Rs')

    #grocery price calculation
    riceprice = int(riceEntry.get()) * 30
    daalprice = int(daalEntry.get()) * 100
    oilprice = int(oilEntry.get()) * 120
    sugarprice = int(sugarEntry.get()) * 50
    teaprice = int(teaEntry.get()) * 140
    wheatprice = int(wheatEntry.get()) * 80

    totalgroceryprice = riceprice + daalprice + oilprice + sugarprice + teaprice + wheatprice

    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, str(totalgroceryprice) + ' Rs')
    grocerytax = totalgroceryprice * 0.05
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax) + 'Rs')

    maazaprice = int(maazaEntry.get()) * 50
    frootiprice = int(frootiEntry.get()) * 20
    dewprice = int(dewEntry.get()) * 30
    pepsiprice = int(pepsiEntry.get()) * 45
    spriteprice = int(spriteEntry.get()) * 90
    cocacolaprice = int(cocacolaEntry.get()) * 80

    totalcolddinksprice = maazaprice + frootiprice + dewprice + pepsiprice + spriteprice + cocacolaprice
    colddrinkspriceEntry.delete(0, END)
    colddrinkspriceEntry.insert(0, str(totalcolddinksprice) + 'Rs')
    colddrinkstax = totalcolddinksprice * 0.08
    colddrinkstaxEntry.delete(0, END)
    colddrinkstaxEntry.insert(0, str(colddrinkstax) + 'Rs')

    totalbill = totalcostmeticprice + totalgroceryprice + totalcolddinksprice + costmetictax + grocerytax + colddrinkstax


#GUI part
root = Tk()
root.title('Retail Billing system')
root.geometry('1270x685')
root.iconbitmap('icon.ico')
headingLabel = Label(root, text='Retail Billing system', font=('times new roman', 30, 'bold')
                     , bg='gray20', fg='gold', bd=12, relief=GROOVE)
headingLabel.pack(fill=X)
customer_detail_frame = LabelFrame(root, text='customer Deatils', font=('time new roman', 15, 'bold')
                                   , fg='gold', bd=8, relief=GROOVE, bg='gray20')

customer_detail_frame.pack(fill=X)
nameLabel = Label(customer_detail_frame, text='Name', font=('time new roman', 15, 'bold',), bg='gray20'
                  , fg='white')

nameLabel.grid(row=0, column=0, padx=20, )

nameEntery = Entry(customer_detail_frame, font=('arial', 15), bd=7, width=18)
nameEntery.grid(row=0, column=1, padx=8)

phoneLabel = Label(customer_detail_frame, text='Phone Number', font=('time new roman', 15, 'bold',), bg='gray20'
                   , fg='white')

phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntery = Entry(customer_detail_frame, font=('arial', 15), bd=7, width=18)
phoneEntery.grid(row=0, column=3, padx=8)

billnumberLabel = Label(customer_detail_frame, text='Bill number', font=('time new roman', 15, 'bold',), bg='gray20'
                        , fg='white')

billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

billnumberEntery = Entry(customer_detail_frame, font=('arial', 15), bd=7, width=18)
billnumberEntery.grid(row=0, column=5, padx=8)

searchButton = Button(customer_detail_frame, text='SEARCH', font=('arial', 12, 'bold'), bd=7,width=10,command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

productsFrame = Frame(root)
productsFrame.pack()

cosmeticsFrame = LabelFrame(productsFrame, text='cosmetics', font=('time new roman', 15, 'bold')
                            , fg='gold', bd=8, relief=GROOVE, bg='gray20')

cosmeticsFrame.grid(row=0, column=0)

bathsoapLabel = Label(cosmeticsFrame, text='Bath soap', font=('time new roman', 15, 'bold',), bg='gray20'
                      , fg='white')
bathsoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky='W')
bathsoapEntry = Entry(cosmeticsFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
bathsoapEntry.grid(row=0, column=1, pady=9, padx=10, sticky='W')
bathsoapEntry.insert(0, 0)

FacecreamLabel = Label(cosmeticsFrame, text='Face cream', font=('time new roman', 15, 'bold',), bg='gray20'
                       , fg='white')
FacecreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky='W')
FacecreamEntry = Entry(cosmeticsFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
FacecreamEntry.grid(row=1, column=1, pady=9, padx=10, sticky='W')
FacecreamEntry.insert(0, 0)

FacewashLabel = Label(cosmeticsFrame, text='Face Wash', font=('time new roman', 15, 'bold',), bg='gray20'
                      , fg='white')
FacewashLabel.grid(row=2, column=0, pady=9, padx=10, sticky='W')
FacewashEntry = Entry(cosmeticsFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
FacewashEntry.grid(row=2, column=1, pady=9, padx=10, sticky='W')
FacewashEntry.insert(0, 0)
hairsprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('time new roman', 15, 'bold',), bg='gray20'
                       , fg='white')
hairsprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky='W')
hairsprayEntry = Entry(cosmeticsFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
hairsprayEntry.grid(row=3, column=1, pady=9, padx=10, sticky='W')
hairsprayEntry.insert(0, 0)
hairgelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('time new roman', 15, 'bold',), bg='gray20'
                     , fg='white')
hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky='W')
hairgelEntry = Entry(cosmeticsFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
hairgelEntry.grid(row=4, column=1, pady=9, padx=10, sticky='W')
hairgelEntry.insert(0, 0)

bodylotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('time new roman', 15, 'bold',), bg='gray20'
                        , fg='white')
bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky='W')
bodylotionEntry = Entry(cosmeticsFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
bodylotionEntry.grid(row=5, column=1, pady=9, padx=10, sticky='W')
bodylotionEntry.insert(0, 0)

groceryFrame = LabelFrame(productsFrame, text='Grocery', font=('time new roman', 15, 'bold')
                          , fg='gold', bd=8, relief=GROOVE, bg='gray20')

groceryFrame.grid(row=0, column=1)

riceLabel = Label(groceryFrame, text='Rice', font=('time new roman', 15, 'bold',), bg='gray20'
                  , fg='white')
riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='W')
riceEntry = Entry(groceryFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
riceEntry.grid(row=0, column=1, pady=9, padx=10, sticky='W')
riceEntry.insert(0, 0)
oilLabel = Label(groceryFrame, text='Oil', font=('time new roman', 15, 'bold',), bg='gray20'
                 , fg='white')
oilLabel.grid(row=1, column=0, pady=9, padx=10, sticky='W')
oilEntry = Entry(groceryFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
oilEntry.grid(row=1, column=1, pady=9, padx=10, sticky='W')
oilEntry.insert(0, 0)

daalLabel = Label(groceryFrame, text='Daal', font=('time new roman', 15, 'bold',), bg='gray20'
                  , fg='white')
daalLabel.grid(row=2, column=0, pady=9, padx=10, sticky='W')
daalEntry = Entry(groceryFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
daalEntry.grid(row=2, column=1, pady=9, padx=10, sticky='W')
daalEntry.insert(0, 0)
wheatLabel = Label(groceryFrame, text='Wheat', font=('time new roman', 15, 'bold',), bg='gray20'
                   , fg='white')
wheatLabel.grid(row=3, column=0, pady=9, padx=10, sticky='W')
wheatEntry = Entry(groceryFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
wheatEntry.grid(row=3, column=1, pady=9, padx=10, sticky='W')
wheatEntry.insert(0, 0)

sugarLabel = Label(groceryFrame, text='Sugar', font=('time new roman', 15, 'bold',), bg='gray20'
                   , fg='white')
sugarLabel.grid(row=4, column=0, pady=9, padx=10, sticky='W')
sugarEntry = Entry(groceryFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
sugarEntry.grid(row=4, column=1, pady=9, padx=10, sticky='W')
sugarEntry.insert(0, 0)

teaLabel = Label(groceryFrame, text='Tea', font=('time new roman', 15, 'bold',), bg='gray20'
                 , fg='white')
teaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='W')
teaEntry = Entry(groceryFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
teaEntry.grid(row=5, column=1, pady=9, padx=10, sticky='W')
teaEntry.insert(0, 0)
drinksFrame = LabelFrame(productsFrame, text='Cold Drink', font=('time new roman', 15, 'bold')
                         , fg='gold', bd=8, relief=GROOVE, bg='gray20')

drinksFrame.grid(row=0, column=2)

maazaLabel = Label(drinksFrame, text='Maaza', font=('time new roman', 15, 'bold',), bg='gray20'
                   , fg='white')
maazaLabel.grid(row=0, column=0, pady=9, padx=10, sticky='W')
maazaEntry = Entry(drinksFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
maazaEntry.grid(row=0, column=1, pady=9, padx=10, sticky='W')
maazaEntry.insert(0, 0)

pepsiLabel = Label(drinksFrame, text='Pepsi', font=('time new roman', 15, 'bold',), bg='gray20'
                   , fg='white')
pepsiLabel.grid(row=1, column=0, pady=9, padx=10, sticky='W')
pepsiEntry = Entry(drinksFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
pepsiEntry.grid(row=1, column=1, pady=9, padx=10, sticky='W')
pepsiEntry.insert(0, 0)
spriteLabel = Label(drinksFrame, text='Sprite', font=('time new roman', 15, 'bold',), bg='gray20'
                    , fg='white')
spriteLabel.grid(row=2, column=0, pady=9, padx=10, sticky='W')
spriteEntry = Entry(drinksFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
spriteEntry.grid(row=2, column=1, pady=9, padx=10, sticky='W')
spriteEntry.insert(0, 0)
frootiLabel = Label(drinksFrame, text='Frooti', font=('time new roman', 15, 'bold',), bg='gray20'
                    , fg='white')
frootiLabel.grid(row=3, column=0, pady=9, padx=10, sticky='W')
frootiEntry = Entry(drinksFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
frootiEntry.grid(row=3, column=1, pady=9, padx=10, sticky='W')
frootiEntry.insert(0, 0)

cocacolaLabel = Label(drinksFrame, text='Coca Cola', font=('time new roman', 15, 'bold',), bg='gray20'
                      , fg='white')
cocacolaLabel.grid(row=4, column=0, pady=9, padx=10, sticky='W')
cocacolaEntry = Entry(drinksFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
cocacolaEntry.grid(row=4, column=1, pady=9, padx=10, sticky='W')
cocacolaEntry.insert(0, 0)

dewLabel = Label(drinksFrame, text='Dew', font=('time new roman', 15, 'bold',), bg='gray20'
                 , fg='white')
dewLabel.grid(row=5, column=0, pady=9, padx=10, sticky='W')
dewEntry = Entry(drinksFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
dewEntry.grid(row=5, column=1, pady=9, padx=10, sticky='W')
dewEntry.insert(0, 0)
billframe = Frame(productsFrame, bd=8, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

billareaLabel = Label(billframe, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE)

billareaLabel.pack(fill=X)
scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(billframe, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(root, text='Bill Menu', font=('time new roman', 15, 'bold')
                           , fg='gold', bd=8, relief=GROOVE, bg='gray20')

billmenuFrame.pack()

costmeticpriceLabel = Label(billmenuFrame, text='Costmetic Price', font=('time new roman', 15, 'bold',), bg='gray20'
                            , fg='white')
costmeticpriceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='W')

costmeticpriceEntry = Entry(billmenuFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
costmeticpriceEntry.grid(row=0, column=1, pady=9, padx=10, sticky='W')

grocerypriceLabel = Label(billmenuFrame, text='Grocery Price', font=('time new roman', 15, 'bold',), bg='gray20'
                          , fg='white')
grocerypriceLabel.grid(row=1, column=0, pady=9, padx=10, sticky='W')

grocerypriceEntry = Entry(billmenuFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
grocerypriceEntry.grid(row=1, column=1, pady=9, padx=10, sticky='W')

colddrinkspriceLabel = Label(billmenuFrame, text='Cold Drinks Price', font=('time new roman', 15, 'bold',), bg='gray20'
                             , fg='white')
colddrinkspriceLabel.grid(row=2, column=0, pady=9, padx=10, sticky='W')

colddrinkspriceEntry = Entry(billmenuFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
colddrinkspriceEntry.grid(row=2, column=1, pady=9, padx=10, sticky='W')

costmetictaxLabel = Label(billmenuFrame, text='Costmetic Tax', font=('time new roman', 15, 'bold',), bg='gray20'
                          , fg='white')
costmetictaxLabel.grid(row=0, column=2, pady=9, padx=10, sticky='W')

costmetictaxEntry = Entry(billmenuFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
costmetictaxEntry.grid(row=0, column=3, pady=9, padx=10)

grocerytaxLabel = Label(billmenuFrame, text='Grocery Tax', font=('time new roman', 15, 'bold',), bg='gray20'
                        , fg='white')
grocerytaxLabel.grid(row=1, column=2, pady=9, padx=10, sticky='W')

grocerytaxEntry = Entry(billmenuFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
grocerytaxEntry.grid(row=1, column=3, pady=9, padx=10, sticky='W')

colddrinkstaxLabel = Label(billmenuFrame, text='Cold Drinks Tax', font=('time new roman', 15, 'bold',), bg='gray20'
                           , fg='white')
colddrinkstaxLabel.grid(row=2, column=2, pady=9, padx=10, sticky='W')

colddrinkstaxEntry = Entry(billmenuFrame, font=('time new roman', 15, 'bold'), width=10, bd=5)
colddrinkstaxEntry.grid(row=2, column=3, pady=9, padx=10, sticky='W')

buttonframe = Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonframe.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonframe, text='Total', font=('arial', 16, 'bold'), bg='gray20', fg='white'
                     , bd=5, width=8, pady=10, command=total)

totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(buttonframe, text='Bill', font=('arial', 16, 'bold'), bg='gray20', fg='white'
                    , bd=5, width=8, pady=10, command=bill_area)

billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(buttonframe, text='Email', font=('arial', 16, 'bold'), bg='gray20', fg='white'
                     , bd=5, width=8, pady=10,command=send_email)

emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton = Button(buttonframe, text='Print', font=('arial', 16, 'bold'), bg='gray20', fg='white'
                     , bd=5, width=8, pady=10,command=print_bill)

printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(buttonframe, text='Clear', font=('arial', 16, 'bold'), bg='gray20', fg='white'
                     , bd=5, width=8, pady=10,command=clear)

clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()
