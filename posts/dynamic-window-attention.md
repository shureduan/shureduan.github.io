# Why a fixed sensor window is the wrong default

*Draft — replace or expand this text before you share the site widely.*

When you fuse video with a vibration or IMU signal, you have to decide how much of the sensor
stream each visual frame gets to look at. The usual answer is a fixed window: two seconds, four
seconds, whatever the validation set likes best. In the TGIF study, that choice turned out to
matter more than the fusion architecture.

A vibration-only classifier makes the problem visible. Accuracy is about 36% below two seconds,
58% between two and four seconds, and 82% between four and eight. An oracle window matched to the
ground-truth action duration — roughly nine seconds — reaches 94%, but that duration is exactly
what you do not know at inference time.

So a fixed window is caught between two failure modes. Short windows measure noise. Long windows
reach across a segment boundary and average two different actions together.

## Letting the segmentation choose the window

Dynamic Window Attention takes the obvious next step: run an initial video-only segmentation,
then use the predicted segment boundaries to define the sensor support for each frame. For a
frame at time $t$ inside predicted segment $s$, the attention is computed over

$$
W(t) = [\, b_{s},\ e_{s} \,]
$$

instead of $[t - \tau, t + \tau]$ for some fixed $\tau$. The video query attends within that
window, and MS-TCN refines the dense action sequence afterwards.

On TGIF this lifted mean accuracy from 91.9% to 92.5% and the Edit score from 89.7% to 91.4%. On
WEAR, concatenated Macro-F1 went from 75.73% to 81.09%, ahead of video-only, early-concatenation,
and fixed-window attention baselines.

The interesting part is not the numbers. It is that the segmentation and the fusion are no longer
independent stages: the first one tells the second where to look.
