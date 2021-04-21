#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
from unittest import TestCase
import allure
from base.httpclient import HttpClient


class TestWeather():
	def setup(self):
		self.host='http://www.weather.com.cn'
		self.ep_path = '/data/cityinfo'
		self.client = HttpClient()

	@allure.story('Test of ShenZhen')
	def test_1(self):
		city_code = '101280601'
		exp_city='深圳'
		self._test(city_code,exp_city)
	@allure.story('Test of BeiJin')
	def test_2(self):
		city_code = '101010100'
		exp_city='北京'
		self._test(city_code,exp_city)
	@allure.story('Test of ShangHai')
	def test_3(self):
		city_code = '101020100'
		exp_city='上海'
		self._test(city_code,exp_city)

	def _test(self,city_code,exp_city):
		url = f'{self.host}{self.ep_path}/{city_code}.html'
		response = self.client.Get(url)
		act_city = response.json()['weatherinfo']['city']
		assert exp_city == act_city