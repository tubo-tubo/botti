# encoding: utf-8


# 単純パーセプトロン・テスト２

class NewNet

	def initialize()
		@x = random_IO # 入力
		@i = 0..(@x.size*@x[0].size)-1 # 入力層(感覚層)
		@k = 1..5 # 出力層(反応層)
		@w = random_weight @k.size, @i.size# 結合重み
		@y = [] # 出力
		@d = set_ans # 教師信号
		@num =0
		p @x
	end

	def main

		while true
			sum=[] # 合計
			@k.each do |o|
				sum.push(0)
				@i.each do |p|
					sum[o-1] += (@w[p][o-1] * @x[p/@x[0].size][p % @x[0].size])
				end
				@y.push(0)
				@y[o-1] = step sum[o-1]
			end
			@k.each do |o|
				@i.each do |p|
					@w[p][o-1] += 0.1 * (@d[o-1]-@y[o-1]) * @x[p/@x[0].size][p % @x[0].size]
				end
			end
			p @d
			p @y
			if @d == @y
				p sum
				p @w
				p @y
				p @d
				break
			elsif @num>=100
				puts "やりすぎ"
				break
			end
			@y = []
			@num+=1
		end
	end

	private

	def random_IO(y=3, x=1)
		out = []
		y.times do
			xin= []
			x.times do
				xin.push(rand(2))
			end
			out.push(xin)
		end
		out
	end

	def set_ans
		o = 1
		_ = 0
		# [[o,o,o,o,o],
		#  [o,_,_,_,_],
		#  [o,o,o,o,o],
		#  [_,_,_,_,o],
		#  [o,o,o,o,o]]
		[1,0,1]
	end

	def random_weight xsize, ysize
		out = []
		ysize.times do
			xin = []
			xsize.times do
				# xin.push(rand-0.5)
				xin.push(rand(10))
			end
			out.push(xin)
		end
		return out
	end

		# 伝達関数
	def step(u, sita = 0)
		if u >= sita
			return 1
		else
			return 0
		end
	end

	def sign(u, sita = 0)
		if u >= sita
			return 1
		else
			return -1
		end
	end

	def sygmoid u
		(1 / (1 + Math::E ** -u))
	end


end

newt = NewNet.new
# newt.main