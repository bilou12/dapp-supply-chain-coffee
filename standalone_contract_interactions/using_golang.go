package main

import (
	"fmt"
	"ioutil"
	"log"

	"github.com/ethereum/go-ethereum/core/types"

	"github.com/ethereum/go-ethereum/ethclient"
)

func main() {
	INFURA_PROJECT_ID := string(ioutil.ReadFile("../.infura-key"))
	client, err := ethclient.Dial("https://rinkeby.infura.io/v3/" + INFURA_PROJECT_ID)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("connected via Infura")

	tx := types.NewTransaction
}
