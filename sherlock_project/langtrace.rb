require 'net/http'
require 'json'

class LangsmithTraceBuilder
  attr_reader :username, :site_data, :proxy, :timeout

  def initialize(username, site_data, proxy: nil, timeout: 60)
    @username = username
    @site_data = site_data
    @proxy = proxy
    @timeout = timeout
  end

  def build_trace
    results_total = {}
    site_data.each do |site_name, site_info|
      url = site_info['url'].gsub('{username}', username)
      response = fetch_url(url)
      results_total[site_name] = analyze_response(response)
    end
    results_total
  end

  private

  def fetch_url(url)
    uri = URI(url)
    http = Net::HTTP.new(uri.host, uri.port, proxy)
    http.read_timeout = timeout
    request = Net::HTTP::Get.new(uri.request_uri)
    http.request(request)
  end

  def analyze_response(response)
    {
      status_code: response.code,
      body: response.body,
      headers: response.to_hash
    }
  end
end

# Example usage:
# site_data = {
#   "example_site" => { "url" => "https://example.com/{username}" }
# }
# trace_builder = LangsmithTraceBuilder.new("testuser", site_data)
# trace = trace_builder.build_trace
# puts trace