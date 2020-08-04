#analzing paying user's behaviors through histograms


df <- data.frame(read.csv("liga_da_4.csv", header = TRUE))
summary(df)
sd(df)

labels_bool <- TRUE
labels_bool <- FALSE



###########
driver <- df$betw_hours
range(driver)
xrange <- 1
breaks <- 500
p1 <- hist(driver, breaks, xlim=c(0, xrange), labels=labels_bool, ylim=c(0, 180), prob=FALSE, col="red",xlab="hours before first purchase")


###########
driver <- df$betw_lp_earn

xrange <- range(driver)[2]
xrange <- 200
breaks <- 200
p1 <- hist(driver, breaks, xlim=c(0, xrange), labels=labels_bool, ylim=c(0, 180), prob=FALSE, col="red",xlab="lp earn before first purchase")


###########
driver <- df$betw_league_cnt

xrange <- range(driver)[2]
xrange <- 10
breaks <- 20
p1 <- hist(driver, breaks, xlim=c(0, xrange), labels=labels_bool, ylim=c(0, 180), prob=FALSE, col="red",xlab="lp earn before first purchase")


###########
driver <- df$betw_count

xrange <- range(driver)[2]
xrange <- 600
breaks <- 100
p1 <- hist(driver, breaks, xlim=c(0, xrange), labels=labels_bool, ylim=c(0, 26), prob=FALSE, col="red",xlab="play counts before first purchase", ylab = "users")

###########
driver1 <- df$betw_avg_f_free
driver3 <- df$betw_avg_f_gem

xrange <- range(driver1)[2]
xrange3 <- range(driver3)[2]
xrange <- 600
breaks1 <- 40
breaks3 <- 10
p1 <- hist(driver1, breaks, xlim=c(0, xrange), labels=labels_bool, ylim=c(0, 60), prob=FALSE, col="red",xlab="free faucet earned before first purchase", ylab = "users")
p3 <- hist(driver3, breaks3, xlim=c(0, 2), labels=labels_bool, ylim=c(0, 120), prob=FALSE, col="red",xlab="gem before first purchase", ylab = "users")

plot(p1, col="red", xlim=c(0,xrange), main="",xlab="avg_bet",ylim=c(0, 80), ylab="free", labels=labels_bool)
plot(p3,  col=rgb(0, 1, 0, 1), xlim=c(0,xrange), add=T, ylim=c(0, 80),xlab="gem", ylab="users", labels=labels_bool)
plot(p3, legend("topright", c("Churn (d+1)", "Stay (d+1)"), col=c("Red", "Green"), lwd=10))

###########avg_bet
xrange <- 1000000
breaks <- 40000
labels_bool <- TRUE
labels_bool <- FALSE

p1 <- hist(df$avg_bet[df['stay']==0], breaks, xlim=c(0, xrange), labels=labels_bool, probability=FALSE)
p2 <- hist(df$avg_bet[df['stay']==1], 2*breaks, xlim=c(0, xrange),labels=labels_bool, probability=FALSE)
plot(p1, col="red", xlim=c(0,xrange), main="",xlab="avg_bet",ylim=c(0, 2000), ylab="users", labels=labels_bool)
plot(p2,  col=rgb(0, 1, 0, 0.5), xlim=c(0,xrange), add=T, ylim=c(0, 2000),xlab="avg_bet", ylab="users", labels=labels_bool)
plot(p2, legend("topright", c("Churn (d+1)", "Stay (d+1)"), col=c("Red", "Green"), lwd=10))



ratio <- p2$counts/(p1$counts+p2$counts)
ratio[is.na(ratio)] <- 0
ratio[is.inf(ratio)] <- 0
plot(ratio, xlim=c(0, 500), ylim=c(0, 1), ,xlab="avg_bet")









