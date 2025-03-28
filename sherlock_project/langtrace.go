package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"time"
)

type LangsmithTraceBuilder struct {
	Username string
	SiteData map[string]map[string]string
	Proxy    *url.URL
	Timeout  time.Duration
}

func NewLangsmithTraceBuilder(username string, siteData map[string]map[string]string, proxy *url.URL, timeout time.Duration) *LangsmithTraceBuilder {
	return &LangsmithTraceBuilder{
		Username: username,
		SiteData: siteData,
		Proxy:    proxy,
		Timeout:  timeout,
	}
}

func (ltb *LangsmithTraceBuilder) BuildTrace() (map[string]map[string]interface{}, error) {
	resultsTotal := make(map[string]map[string]interface{})
	for siteName, siteInfo := range ltb.SiteData {
		url := siteInfo["url"]
		url = replaceUsername(url, ltb.Username)
		response, err := ltb.fetchURL(url)
		if err != nil {
			return nil, err
		}
		resultsTotal[siteName] = ltb.analyzeResponse(response)
	}
	return resultsTotal, nil
}

func replaceUsername(url, username string) string {
	return strings.Replace(url, "{username}", username, -1)
}

func (ltb *LangsmithTraceBuilder) fetchURL(urlStr string) (*http.Response, error) {
	client := &http.Client{
		Timeout: ltb.Timeout,
	}
	if ltb.Proxy != nil {
		client.Transport = &http.Transport{
			Proxy: http.ProxyURL(ltb.Proxy),
		}
	}
	req, err := http.NewRequest("GET", urlStr, nil)
	if err != nil {
		return nil, err
	}
	return client.Do(req)
}

func (ltb *LangsmithTraceBuilder) analyzeResponse(response *http.Response) map[string]interface{} {
	defer response.Body.Close()
	body, _ := ioutil.ReadAll(response.Body)
	headers := make(map[string][]string)
	for k, v := range response.Header {
		headers[k] = v
	}
	return map[string]interface{}{
		"status_code": response.StatusCode,
		"body":        string(body),
		"headers":     headers,
	}
}

func main() {
	siteData := map[string]map[string]string{
		"example_site": {"url": "https://example.com/{username}"},
	}
	traceBuilder := NewLangsmithTraceBuilder("testuser", siteData, nil, 60*time.Second)
	trace, err := traceBuilder.BuildTrace()
	if err != nil {
		fmt.Println("Error building trace:", err)
		return
	}
	traceJSON, _ := json.MarshalIndent(trace, "", "  ")
	fmt.Println(string(traceJSON))
}