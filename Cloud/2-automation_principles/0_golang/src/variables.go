package main

const percentage = 0.9

var fruit string

var car string = "bmw"

var score = 100

var brand, model string = "mercedez", "volvo"

var temperature = func() int { return 85 }

func assignment() {
	fruit = "google"
	// := infers data type
	subject_score := 70
	extra_points := 20
	lost_points := 15

	subject_score += extra_points // this sums
	subject_score -= lost_points

	name, age, height, weight := "bla", 89, 8273, 6262627281
	println(name, age, height, weight)
}
