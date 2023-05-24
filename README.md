# NameSpotter
NameSpotter is a powerful but easy Python program designed to efficiently scan multiple websites and social media platforms to check the availability of a specific username. Utilizing the power of multithreading, NameSpotter maximizes performance by concurrently scanning dozens of websites, allowing you to quickly determine if a username is registered or available.

## Installation
1. Clone repository: `git clone https://github.com/simplylu/namespotter`
2. cd into directory: `cd namespotter`
3. Install requirements: `pip3 install -r requirements.txt`

## Usage
Run: `python3 namespotter.py <username>`

Sample run:
```
user@client ~/X/Y/NameSpotter (main)> python3 namespotter.py s1mplylu
     _   __                    _____             __  __           
    / | / /___ _____ ___  ___ / ___/____  ____  / /_/ /____  _____
   /  |/ / __ `/ __ `__ \/ _ \__ \/ __ \/ __ \/ __/ __/ _ \/ ___/
  / /|  / /_/ / / / / / /  __/__/ / /_/ / /_/ / /_/ /_/  __/ /    
 /_/ |_/\__,_/_/ /_/ /_/\___/____/ .___/\____/\__/\__/\___/_/     
(c) 2023 by simplylu (@s1mplylu)/_/ 
Progress: 56/56 - reverbnation        
Found on ello :: https://ello.co/s1mplylu
Found on paypal :: https://www.paypal.com/paypalme/s1mplylu
Found on instagram :: https://www.instagram.com/s1mplylu/
Found on tiktok :: https://www.tiktok.com/@s1mplylu?lang=en

Found 4 services for username s1mplylu
Took 5.33s to run
Ch33rs, Lu <3
```

Some services may utilize firewalls or services like CloudFront / CloudFlare. If you suspect to get a wrong result for a service, try to run it through a Proxy, VPN or Tor.

If you wanna test the code for it's functionality, run `python3 test.py` to check if everything works. You might get errors for above mentioned services using extra security mechanisms.

## Difficult services (help needed)
Everything which is somehow related to Google and companies is quite annoying to check.
Currently, there are problems to implement checks for the following services. Feel free to try and contribute.
- twitter.com
- reddit.com
- 500px.com
- onlyfans.com (one security key gets calculated in JS and without it, one can't query the API the website uses to check for an existing profile...)
- tripadvisor.com (Implemented, curl logic does work, but in Python the requests are timing out.)
- creativemarket.com (CloudFront / Cloudflare...)

There are a couple of services in `/services` that start with an underscore. Those are ignored by the program and most probably services, that have been implemented, but do not work for any reason. Feel free to check them out and make them work.

## Contribute a new Service
This is a blueprint of a new service. Copy it to a new file in `/services`.:
```py
import requests

__info__ = "Put one sentence describing the service here."

def check(username: str) -> bool:
  url: str = f"<url to service goes here, replace actual username with {username}"
  req: requests.Response = requests.get(url)
  return ("<pattern>" in req.text, url)
  # or
  return (req.status_code // 100 == 2, url)
```

Please remember to always return a tuple of the form `Tuple[bool, str]`. The `bool` describes whether the username exists for that service or not. The `str` contains the URL to that user of that service. If you don't use that return type, userscan will probably fail.

I've used two methods, depending on how the service responds to the request of non-existing usernames. 

The first one is checking the status code. If it is not 2XX, it might be something like 4XX or 5XX and the user probably does not exist.

Another method is to compare a sucessful response and the response for the request of a non-existing user. Maybe you can find a pattern being part of only one response, which you can use to decide whether the user exists, or not.

This is not failsafe and working services might not work in the future. That's what testing is for.

### Testing
Add the service (name must be the exact as the filename, without the `.py` extension), an existing username, as well as a non-existing username to test.py. Just copy an existing section, it's quite easy.

After that, you can test the new service by running `python3 test.py <name of the service>`. If you added for example `spotify.py` to the `services` folder, and the respective section in `test.py`, you can check the service by calling `python3 test.py spotify`.

When running `python3 test.py`, it'll test every available service. This is good for checking if the whole repository works, but for testing single / new services, take the above approach.

## Currently available services
### aboutme
> About.me is a personal branding platform that allows individuals to create a centralized online profile, showcasing their professional background, interests, and social media presence.
### bandcamp
> Bandcamp.com is a music-focused platform that empowers independent artists to showcase, sell, and distribute their music directly to fans, fostering a supportive and direct connection between musicians and their audience.
### bebee
> BeBee.com is a professional networking platform that combines elements of social media and job searching, allowing users to showcase their personal brand, connect with industry professionals, and discover career opportunities in a vibrant community.
### behance
> Behance.net is a leading online platform for creative professionals, where artists, designers, and creators can showcase their portfolios, gain exposure, and connect with potential clients and collaborators.
### blipfm
> Blip.fm was a social music streaming platform that allowed users to discover, share, and listen to music in a personalized radio-style format, but it is no longer in active operation as of 2021.
### blogger
> Blogspot.com, also known as Blogger, is a popular blogging platform that enables users to create and publish their own blogs with ease, offering various customization options and integration with Google services.
### buzzfeed
> Buzzfeed.com is a digital media platform known for its entertaining and shareable content, offering a mix of news, quizzes, lists, and viral articles that cater to a wide range of interests and pop culture trends.
### campsite
> Campsite.bio is an all-in-one link management platform designed for creators, influencers, and businesses, allowing them to create a customizable landing page with multiple links, social media profiles, and promotional content to enhance their online presence and engagement.
### cashapp
> Cash.me (now known as Cash App) is a mobile payment platform that enables users to send and receive money, make purchases, and manage their finances through a simple and user-friendly interface.
### colourlovers
> Colourlovers.com is a vibrant online community and resource for color inspiration, providing a platform for users to explore, create, and share color palettes, patterns, and designs.
### contactinbio
> Contactin.bio is a comprehensive contact management platform that allows users to create a customized landing page with multiple contact options, making it easy for others to connect with them through various communication channels.
### dailymotion
> Dailymotion.com is a video-sharing platform that offers a diverse range of user-generated and professional content, allowing users to discover, watch, and share videos across various topics and genres.
### designspiration
> Designspiration.com is a visual inspiration platform that curates a wide range of design-related content, including images, projects, and ideas, serving as a valuable resource for designers seeking creative inspiration.
### deviantart
> DeviantArt.com is an online community and art platform that enables artists of various genres to showcase their artwork, connect with fellow creators, and engage in a supportive environment for artistic expression and appreciation.
### disqus
> Disqus.com is a widely-used commenting platform that allows website owners to integrate a robust and interactive commenting system into their websites, fostering engagement and discussion among visitors.
### douban
> Douban.com is a Chinese social networking platform that combines elements of film, book, and music reviews, fostering discussions and recommendations among users based on their shared interests.
### dribble
> Dribbble.com is an online community and platform for designers, providing a space to showcase their creative work, gain inspiration, and connect with other design professionals and potential clients.
### ello
> Ello.co is a social networking platform that emphasizes ad-free, creative expression and community engagement, providing a space for artists, designers, and enthusiasts to share their work and connect with like-minded individuals.
### elpha
> Elpha.com is an online community and platform designed for women in tech and entrepreneurship, providing a supportive space for networking, mentorship, and knowledge sharing to empower women in their professional journeys.
### etsy
> Etsy.com is an online marketplace that connects independent sellers and buyers, offering a wide range of unique and handmade products, vintage items, and craft supplies.
### flickr
> Flickr.com is a popular photo-sharing platform that enables users to upload, organize, and share their images with others, while also providing a vibrant community for photography enthusiasts to discover and engage with diverse visual content.
### flipboard
> Flipboard.com is a personalized news aggregation platform that curates and delivers articles, stories, and multimedia content based on users' interests, allowing for a tailored and immersive reading experience.
### gaiaonline
> GaiaOnline.com is an online community and virtual world where users can create avatars, engage in role-playing, and interact with other members through forums, games, and various social activities.
### giphy
> YouTube.com is a widely-used video-sharing platform that allows users to upload, watch, and interact with a vast array of user-generated and professional content spanning various topics and genres.
### github
> Github.com is a widely-used web-based platform that provides hosting for software development projects, allowing developers to collaborate, version control their code, and track issues in a streamlined and accessible manner.
### goodreads
> Goodreads.com is a social platform for book lovers, offering a vast database of user-generated book reviews, recommendations, and a community-driven space for discussing literature and discovering new reads.
### gravatar
> Gravatar.com is a globally recognized avatar service that allows users to associate a unique profile picture with their email address, which is automatically displayed on various websites and platforms that support Gravatar integration.
### gumroad
> Gumroad.com is an e-commerce platform that empowers creators and small businesses to sell digital products, subscriptions, and physical goods directly to their audience with ease.
### houzz
> Houzz.com is a comprehensive home improvement and design platform that offers inspiration, product recommendations, and professional services to homeowners, serving as a hub for all things related to home remodeling and decoration.
### hubpages
> HubPages.com is an online publishing platform where users can create and share informative articles on various topics, engage with a community of writers, and earn revenue through advertising and affiliate programs.
### ifttt
> IFTTT.com is an automation platform that enables users to create connections between different apps and devices, allowing them to automate tasks and workflows based on triggers and actions, simplifying digital interactions.
### instagram
> Instagram.com is a popular social media platform that emphasizes visual content, enabling users to share photos and videos, discover creative inspiration, and engage with a global community.
### instructables
> Instructables.com is a platform that allows users to discover, create, and share step-by-step DIY projects and tutorials across a wide range of topics, promoting creativity and knowledge-sharing in a vibrant community.
### italki
> italki.com is an online language learning platform that connects language learners with qualified tutors for personalized language lessons through video chat, helping users improve their language skills from the comfort of their own homes.
### keybase
> Keybase.io is a platform that combines encrypted messaging, file sharing, and identity verification, providing a secure and user-friendly environment for communication and collaboration.
### kongregate
> Kongregate.com is an online gaming platform that offers a vast collection of free-to-play games, ranging from casual to more complex genres, providing an entertaining and community-driven gaming experience.
### lastfm
> Last.fm is a music streaming and recommendation platform that tracks users' listening habits, provides personalized music recommendations, and connects music enthusiasts with similar tastes in an engaging online community.
### letterboxd
> Letterboxd.com is a film-focused social networking platform that allows users to discover, rate, and review movies, create personalized film diaries, and engage in discussions with a passionate community of cinephiles.
### likee
> Likee.video is a dynamic short video platform that allows users to create and share creative videos, discover trending content, and engage with a global community through innovative video editing features and interactive challenges.
### linktree
> Linktr.ee is a popular link management tool that allows users, particularly content creators and businesses, to create a customizable landing page containing multiple links to various online platforms and resources.
### livejournal
> LiveJournal.com is a long-standing blogging platform that combines social networking features, allowing users to publish personal journal entries, connect with friends, and participate in communities, fostering online expression and interaction.
### lnkbio
> Lnk.bio is a link management platform that allows users to create a customized landing page with multiple links, making it easier to share and navigate various online profiles and content in one central location.
### medium
> Medium.com is a popular online publishing platform where writers, journalists, and experts can share their articles and stories with a wide audience, while fostering a community of readers and facilitating thoughtful discussions.
### milkshake
> Milkshake.app is a user-friendly mobile website builder that enables users to create stylish and personalized single-page websites directly from their smartphones, perfect for showcasing portfolios, businesses, and personal brands.
### mix
> Mix.com is a content discovery platform that personalizes and recommends articles, videos, and other web content based on users' interests, providing a convenient way to explore and save interesting content from across the web.
### myanimelist
> MyAnimeList.com is a popular online platform for anime and manga enthusiasts, offering a comprehensive database, user reviews, and community features to discover, track, and discuss their favorite anime and manga titles.
### myspace
> Myspace.com is a former social networking platform that gained popularity in the early 2000s, allowing users to create personal profiles, connect with friends, and discover music and entertainment content.
### newgrounds
> Newgrounds.com is an online entertainment platform that hosts user-generated content such as animations, games, and artwork, providing a space for creativity and community interaction within the digital arts.
### pastebin
> Pastebin.com is an online platform that allows users to store and share text snippets or code snippets, providing a convenient way to share and collaborate on textual content.
### patreon
> Patreon.com is a membership platform that enables creators to receive recurring financial support from their fans and followers, allowing them to monetize their content and engage with a dedicated community.
### paypal
> PayPal.me is a personalized payment link service provided by PayPal, allowing users to easily request and receive money from others by sharing a unique link associated with their PayPal account.
### picsart
> PicsArt.com is a popular creative platform that offers a suite of powerful photo editing tools, artistic filters, and a vibrant community for users to explore, enhance, and share their photos and digital artwork.
### pinterest
> Pinterest.com is a visually-focused social media platform where users can discover, save, and share inspiring ideas and images across a wide range of interests and topics.
### quora
> Quora.com is a question-and-answer platform where users can ask questions, share knowledge, and engage in discussions on a wide range of topics, tapping into the collective wisdom and expertise of a diverse community.
### reverbnation
> ReverbNation.com is a music-focused platform that provides tools for artists to promote their music, connect with fans, book gigs, and access industry opportunities, supporting independent musicians in their career development.
### roblox
> Roblox.com is an immersive online platform that allows users to create, play, and share games and virtual experiences, fostering a vibrant community of game developers and players.
### rumble
> Rumble.com is a video-sharing platform that emphasizes user-generated content, allowing creators to upload, share, and monetize their videos while offering a diverse range of content for viewers to explore.
### scribd
> Scribd.com is a digital library and document sharing platform offering a vast collection of books, audiobooks, magazines, and documents, accessible through a subscription model, providing a comprehensive resource for reading and research.
### skyrock
> Skyrock.com is a social networking platform that allows users to create personalized blogs, share multimedia content, and connect with a community of users with shared interests.
### slack
> Slack.com is a widely-used collaboration platform that facilitates team communication, file sharing, and project management, enhancing productivity and streamlining workflows for organizations of all sizes.
### slideshare
> Slideshare.net is a platform for sharing and discovering professional presentations, documents, and infographics, providing a valuable resource for knowledge sharing and learning across various industries and topics.
### soundcloud
> SoundCloud.com is a popular online audio distribution platform that enables musicians, podcasters, and other audio creators to upload, share, and promote their audio content while connecting with a diverse community of listeners.
### spotify
> Spotify.com is a leading music streaming platform that offers a vast library of songs, podcasts, and audio content, allowing users to discover, stream, and create personalized playlists tailored to their musical preferences.
### steamcommunity
> Steamcommunity.com is a social hub integrated with the Steam gaming platform, enabling gamers to connect, share content, join communities, and engage in discussions related to gaming and game development.
### steemit
> Steemit.com is a blockchain-based social media platform where users can create, curate, and engage with content, earning cryptocurrency rewards for their contributions.
### substack
> Substack.com is a newsletter platform that empowers writers and journalists to publish and monetize their content directly, fostering a direct connection with their audience and providing a subscription-based model for readers.
### tiktok
> TikTok.com is a highly engaging video-sharing platform known for its short-form and creative content, where users can create, discover, and share entertaining videos across a wide range of topics and trends.
### trakttv
> Trakt.tv is a platform dedicated to tracking and organizing users' TV shows and movies, offering features such as personalized recommendations, watchlist management, and social interactions with other entertainment enthusiasts.
### tumblr
> Tumblr.com is a microblogging and social media platform where users can create and share multimedia posts, follow other blogs, and engage in a community that spans a diverse range of interests and creative expression.
### twitch
> Twitch.tv is a popular live streaming platform primarily focused on video game streaming and esports content, but also encompassing a wide range of creative arts and entertainment categories.
### untappd
> Untappd.com is a social networking platform for beer enthusiasts, allowing users to discover, rate, and share their favorite beers, explore new breweries, and connect with fellow beer lovers.
### vimeo
> Vimeo.com is a video-sharing platform that focuses on high-quality and creative content, providing a space for artists, filmmakers, and professionals to showcase their work and connect with a community of like-minded individuals.
### vk
> VK.com, also known as VKontakte, is a social networking platform that connects users, primarily from Russia and neighboring countries, enabling them to communicate, share media, join communities, and discover entertainment content.
### wattpad
> Wattpad.com is an online storytelling community where users can read, write, and share a wide range of original stories, allowing aspiring writers to showcase their work and engage with a global audience.
### wikipedia
> Wikipedia.org is a vast collaborative online encyclopedia that provides free, reliable, and crowdsourced information on an extensive range of subjects.
### wordpress
> WordPress.com is a user-friendly online platform that allows individuals and businesses to create and host websites or blogs without the need for advanced coding knowledge.
### xing
> Xing.com is a professional networking platform that facilitates business connections, career development, and industry networking, enabling users to showcase their professional profiles and engage with a global community of professionals.
### ycombinator
> News.ycombinator.com is a community-driven platform that features a curated selection of technology news, articles, and discussions, showcasing the latest developments and insights from the tech industry and beyond.
### youtube
> YouTube.com is a widely-used video-sharing platform that allows users to upload, watch, and interact with a vast array of user-generated and professional content spanning various topics and genres.