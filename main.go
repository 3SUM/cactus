package main

import (
	"fmt"
	"log"
	"os"

	"github.com/AlecAivazis/survey/v2"
	"github.com/joho/godotenv"
	"github.com/mbndr/figlet4go"
)

// vars
var (
	appVersion = "2.0"
	appDate    = "2022-24-05"
	username   = ""
	password   = ""
	region     = ""
)

// Attempt to load .env file
func init() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}
}

func main() {
	// Print pretty headers
	ascii := figlet4go.NewAsciiRender()
	options := figlet4go.NewRenderOptions()
	options.FontColor = []figlet4go.Color{
		figlet4go.ColorRed,
	}
	renderStr, _ := ascii.RenderOpts(" Cactus v"+appVersion, options)
	fmt.Print(renderStr)
	fmt.Println("Welcome to Cactus!\nApp version:", appVersion, "/ Build date:", appDate)

	// Begin gathering Riot ID information
	askUsername()
	askPassword()
	askRegion()
}

func askUsername() {
	if username := os.Getenv("USERNAME"); username != "" {
		fmt.Println("Riot ID username loaded from .env!")
		return
	}

	prompt := &survey.Input{
		Message: "Input Riot ID username:",
		Help:    "Riot ID username is required to run Cactus",
	}
	survey.AskOne(prompt, &username, survey.WithValidator(survey.Required))
}

func askPassword() {
	if password := os.Getenv("PASSWORD"); password != "" {
		fmt.Println("Riot ID password loaded from .env!")
		return
	}

	prompt := &survey.Password{
		Message: "Input Riot ID password:",
		Help:    "Riot ID password is required to run Cactus",
	}
	survey.AskOne(prompt, &password, survey.WithValidator(survey.Required))
}

func askRegion() {
	prompt := &survey.Select{
		Message: "Choose Riot ID region:",
		Options: []string{"NA", "EUW", "EUNE", "BR"},
	}
	survey.AskOne(prompt, &region, survey.WithValidator(survey.Required))
}
