from typing import Any
class IntGEZ:  #greter and equal than zero
	# campi dati:
	# _value:int

	def __init__(self, v:int):
		if not isinstance(v, (int, IntGEZ) ):
			raise ValueError(f"Value v must be an int or an IntGEZ")
		if v < 0:
			raise ValueError(f"Value v must be >= 0, now {v}")
		self._value = v.valore() if isinstance(v, IntGEZ) else v

	def valore(self)->int:
		return self._value

	def __hash__(self)->int:
		return hash(self.valore())
	
	def __eq__(self, other:Any)->bool:
		if other is None:
			return False

		if not isinstance(other, type(self)):
			# try to cast other to type(self) using available __init__():
			try:
				other = type(self)(other)
			except:
				return False
		
		if hash(self) != hash(other):
			return False
		else:
			return self.valore() == other.valore()


	def __lt__(self, other:Any)->bool:
		if not isinstance(other, IntGEZ):
			try:
				other = IntGEZ(other)
			except:
				raise TypeError(f"Operator < not defined between {type(self)} and {type(other)}")
		return self.valore() < other.valore()

	def __le__(self, other)->bool:
		if not isinstance(other, type(self)):
			try:
				other = type(self)(other)
			except:
				raise TypeError(f"Operator < not defined between {type(self)} and {type(other)}")
		return self.valore() <= other.valore()

	def __gt__(self, other):
		if not isinstance(other, type(self)):
			try:
				other = type(self)(other)
			except:
				raise TypeError(f"Operator < not defined between {type(self)} and {type(other)}")
		return self.valore() > other.valore()

	def __ge__(self, other):
		if not isinstance(other, type(self)):
			try:
				other = type(self)(other)
			except:
				raise TypeError(f"Operator < not defined between {type(self)} and {type(other)}")
		return self.valore() >= other.valore()


	def __repr__(self)->str:
		return repr(self.valore())

	def __add__(self, other):
		ov:int = other.valore() if isinstance(other, type(self)) else other
		return type(self)(self.valore() + ov)

	def __sub__(self, other):
		ov:int = other.valore() if isinstance(other, type(self)) else other
		return type(self)(self.valore() - ov)