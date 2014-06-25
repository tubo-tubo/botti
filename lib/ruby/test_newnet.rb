# encoding: utf-8

	# 二層・単純パーセプトロンtest

	i = [0,1,2,3]
	k = [0,1,2,3,4,5]
	w = []
	sum =[]
	y = []
	x = [-1,100,80,6]
	d = [0,0,1,1,0,1]
	puts "答 #{d}"
	num = 1

	def step(x)
		if x >= 0
			return 1
		else
			return 0
		end
	end


	i.each do
		wk = []
		k.each do
			wk.push(rand(2)-0.5)
		end
		w.push(wk)
	end

	while true
		k.each do |o|
			sum.push(0)
			i.each do |p|
				sum[o] += (w[p][o] * x[p])
			end
			y.push(0)
			y[o] = step(sum[o])
		end
		k.each do |o|
			i.each do |p|
				w[p][o] += 0.00001 * (d[o]-y[o]) * x[p]
			end
		end
		puts "解答 #{y}"
		if y == d
			puts "#{num}回"
			break
		end
		y = []
		num+=1
		if num>=1000
			puts "停止"
			# とりあえず無限ループ防止
			break
		end
	end

	p w
