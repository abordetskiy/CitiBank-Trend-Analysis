####  Maps:
In general, the CitiBike program seems to be utilized more in higher income areas. Population across Jersey City is relatively consistent, so this may be due to a generally higher income in the Downtown area, where shorter distances and more locations may also support more usage of the CitiBike system. There are a substantial number of trips ending in Manhattan, even though it would require using bridges, tunnels, or ferries and taking much longer trips. This is especially true for Grove St. PATH (the highest volume Start Station in Jersey City). It does seem, however, that most bikes which start in Jersey City end up either staying in, or returning to Jersey City.

#### Trip Analysis Over Time:
Average trip duration is consistent from 2017-2019, and the number of trips steadily rose each year. In 2020, however, the number of trips went down, whereas average trip duration doubled from the previous year. The longest trips seem to start at 2am; this may be a result of early work shifts, depending on the jobs available in downtown Jersey City or Manhattan. This trend is less profound in 2020 but is much more consistent in previous years. This may suggest more people suddenly using CitiBike as a primary form of transportation in 2020 across the board, possibly influenced by the Covid-19 pandemic.

#### Demographic Charts:  
Male Subscribers make up the majority of Bikers, while younger and older (~20 year-old and 50+ year-old) Bikers take longer trips. This is especially true for Customers, who seem to justify longer rides in general. This makes sense as Subscribers likely have a consistent route in mind within the 45-minute time limit – making the subscription worth the annual price. The youngest women take the longest rides on average, but this trend starts to equalize between genders at around age 25.

#### Technical Notes - Data Cleaning: 
Due to unrealistic input into the Birth Year field (resulting in supposed 135-year-old Bikers) we have limited the age category to 80 years of age. The age category for 51 year-olds (Birth Year 1999) was significantly larger than those surrounding it. This started in the 2018 data set, suggesting that it was set as the default, or that many people arbitrarily chose this option. The spike has been removed from the data showing Age demographics.

One major issue was multiple “trips” at the same time for the same Bike ID, so we have selected a single trip for each Bike ID and Trip Time pair based on the Minimum Start Time and Maximum Stop Time if there’s an overlap.
