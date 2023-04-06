path = path[:-1] # This is not needed and cuts last character
return urlunparse((scheme, netloc, path,
                  params, query, fragment))