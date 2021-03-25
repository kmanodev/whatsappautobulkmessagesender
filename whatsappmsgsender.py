from selenium import webdriver
browser= webdriver.Chrome('/home/manouser/software/chromedriver')
browser.get('http://web.whatsapp.com')
input('Enter any key after QR scan')

class main():
	def send(self):
		name=input('Enter the name')
		user=browser.find_element_by_xpath('//span[@title="{}"]'.format(name))
		user.click()

		message=input("enter your msg : ")
		count=int(input("how many times want you sent : "))

		msgbox=browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		for i in range(count):
			msgbox.send_keys(message)
			button=browser.find_element_by_class_name('_1E0Oz')
			button.click()
		print('Completed')
		ret=input("are you want to send msg again(y/n) : ")
		if ret=='y':
			main().send()


main().send()
print('Completed all program')
