from selenium import webdriver
from time import sleep
from secret import login_id,pw,username



class InstaBot:
	def __init__(self, username, login_id, password):
		self.driver = webdriver.Chrome()
		self.driver.get("https://instagram.com")
		sleep(2)
		self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click() 
		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(login_id)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
			.send_keys(pw)
		self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
		sleep(2)
		self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')\
			.click()
		sleep(2)
		self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
			.click()
		sleep(2)
		#/html/body/div[4]/div/div/div[3]/button[2]




	def get_names(self):
		sleep(2)

		scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")    	
		last_ht,ht = 0, 1
		while last_ht != ht:
			last_ht = ht
			sleep(1)
			ht = self.driver.execute_script("""
				arguments[0].scrollTo(0,arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""",scroll_box	)

		links = scroll_box.find_elements_by_tag_name('a')
		names = [name.text for name in links if name != '']

		self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button/div")\
			.click()
		#names = self.driver.execute_script(links.getText())

		return names


	def get_unfollowers(self, username):


		self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(username))\
			.click()
		sleep(3)
		self.driver.find_element_by_xpath("//a[contains(@href, '/following')]")\
			.click()
		sleep(2)

		following = self.get_names()

		self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]")\
			.click()
		sleep(2)

		followers = self.get_names()

		unfollowers = [user for user in following if user not in followers]

		print(unfollowers)
		print(len(unfollowers))

		#self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')\
		#	.click()

		#self.driver.find_element_by_xpath('')\
		#	.click()

		#sleep(2)

		self.driver.close()


if __name__ == '__main__':

	my_bot = InstaBot( username, login_id, pw )
	my_bot.get_unfollowers(username)

