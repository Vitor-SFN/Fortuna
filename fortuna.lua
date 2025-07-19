math.randomseed(os.time())

--implementando orientação a objetos em Lua
Board = { coins = { nil, nil, nil, nil, nil } }

--método para a contrução de novas mesas
function Board:new(o)
	o = o or {} --nova instância do objeto
	setmetatable(o, self) -- Board como metatabela de object
	self.__index = self
	return o
end

function Board:show()
	print(table.concat(self.coins, "  "))
end

-- Criar o Board:dice que gera sequencialmente o ante-flop, flop, turn
-- e river
function Board:dice()
	if self.coins[1] == nil or self.coins[2] == nil then
		self.coins[1] = self.coins[1] or math.random(2)
		self.coins[2] = self.coins[2] or math.random(2)
		return
	end

	if self.coins[3] == nil then
		self.coins[3] = math.random(2)
		return
	end

	if self.coins[4] == nil then
		self.coins[4] = math.random(2)
		return
	end

	if self.coins[5] == nil then
		self.coins[5] = math.random(2)
		return
	end
end

Player = { coins = { nil, nil, nil, nil, nil }, name = nil, cash = 1000 }

function Player:new(o)
	o = o or {}
	setmetatable(o, self)
	self.__index = self
	return o
end

function Player:hand(hand)
	self.coins = hand
end

mesa = Board:new()
for i = 1, 4 do
	mesa:dice()
	mesa:show()
end
